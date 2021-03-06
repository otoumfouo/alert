from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from datetime import datetime, date
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from dateutil import rrule
from datetime import date
from rest_framework import viewsets
from .serializers import *

# Create your views here.
@login_required
def index(request):
    alerts = Alert.objects.all().order_by('datedebut')
    return render(request, 'index.html', locals())


@login_required
def create(request):
    form = AlertsForm(request.POST or None, request.FILES or None)
    return render(request, 'event/form.html', locals())


@login_required
def alertList(request):
    alerts = Alert.objects.all()
    return render(request, 'event/index.html', locals())


@login_required
def dash_pie(request, start, end):
    # def dash_pie(request, start, end):
    start = datetime.strptime(start, "%Y-%m-%d").date()
    end = datetime.strptime(end, "%Y-%m-%d").date()
    source_informations = Capteur_alert.objects.all()
    print(start.strftime(("%d.%m.%Y %H:%M:%S")))
    print(end.strftime(("%d.%m.%Y %H:%M:%S")))
    label = []
    series = []
    data = []
    for source in source_informations:
        value = Alert.objects.filter(source_information=source).count()
        '''value = Alert.objects.filter(source_information=source)\
            .filter(datedebut__range=[start, end])\
            .count()'''
        series.append(value)
        label.append(source.libelle)
    data.append({"label": label, "series": series})
    return JsonResponse(data, safe=False)


@login_required
def dash_line(request, start, end):
    start = datetime.strptime(start, "%Y-%m-%d").date()
    end = datetime.strptime(end, "%Y-%m-%d").date()

    type_alerts = Type_alert.objects.all()
    nbre_alerts = Alert.objects.count()

    source_informations = Capteur_alert.objects.all()
    data = {};
    series = {};
    infos = []
    values = []
    axies = []
    valTotal = []
    for typeA in type_alerts:
        axies.append(typeA.libelle)

    for source in source_informations:

        values = []
        for typeA in type_alerts:
            #axies.append(typeA.libelle)
            alerts = Alert.objects.filter(type=typeA).filter(source_information=source)\
                 .count()
            '''alerts = Alert.objects.filter(type=typeA).filter(source_information=source)\
                .filter(datedebut__range=[start.strftime(("%Y-%m-%d %H:%M:%S")), end.strftime(("%Y-%m-%d %H:%M:%S"))])\
                .count()'''
            values.append(alerts)
            #series["name"] = source.libelle
        infos.append({'name': source.libelle,
                             'data': values,
                             'axies': axies,
                             'total': nbre_alerts
                              })
            #series["data"] =values
        #infos.append(series)


    return JsonResponse(infos, safe=False)


class AlertCreateView(LoginRequiredMixin, CreateView):
    model = Alert
    form_class = AlertsForm

    template_name = 'event/form.html'

    success_url = reverse_lazy('list')

    """def get(self, request,  *args, **kwargs) :
        self.object = self.get_object(queryset=Requisition.objects.all())
        return super().get(request,*args, **kwargs)"""

    def get_context_data(self, **kwargs):
        data = super(AlertCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['alertDegats'] = AlertDegatFormSet(self.request.POST, self.request.FILES,
                                                    instance=self.object, prefix="form_set")
            '''data['fichiers'] = AlertFichierFormSet(self.request.POST, self.request.FILES,
                                                   instance=self.object)'''
            # print(data['fichiers'])
        else:
            data['alertDegats'] = AlertDegatFormSet(instance=self.object, prefix="form_set")
            # data['fichiers'] = AlertFichierFormSet(instance=self.object, prefix="form_fichier_set")

        return data

    def form_valid(self, form):
        context = self.get_context_data(form=form)

        formset = context['alertDegats']
        # formset_fichier = context['fichiers']

        if formset.is_valid():
            form.instance.user = self.request.user
            response = super().form_valid(form)
            self.object.save()
            formset.instance = self.object
            # formset_fichier.instance = self.object

            formset.save()
            # formset_fichier.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().form_invalid(form)


class AlertUpdateView(LoginRequiredMixin, UpdateView):
    model = Alert
    form_class = AlertsForm
    template_name = 'event/form.html'
    success_url = reverse_lazy('list')

    """def get(self, request,  *args, **kwargs) :
        self.object = self.get_object(queryset=Requisition.objects.all())
        return super().get(request,*args, **kwargs)"""

    def get_context_data(self, **kwargs):
        data = super(AlertUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['alertDegats'] = AlertDegatFormSet(self.request.POST, self.request.FILES,
                                                    instance=self.object, prefix="form_set")
            '''data['fichiers'] = AlertFichierFormSet(self.request.POST, self.request.FILES,
                                                   instance=self.object)'''

        else:
            data['alertDegats'] = AlertDegatFormSet(instance=self.object, prefix="form_set")
            '''data['fichiers'] = AlertFichierFormSet(instance=self.object, prefix="form_fichier_set")'''

        return data

    def form_valid(self, form):
        context = self.get_context_data(form=form)

        formset = context['alertDegats']
        # formset_fichier = context['fichiers']
        # print(formset_fichier)
        if formset.is_valid():
            form.instance.user = self.request.user
            response = super().form_valid(form)
            self.object.save()
            formset.instance = self.object
            # formset_fichier.instance = self.object
            # print(formset_fichier)
            formset.save()
            # formset_fichier.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().form_invalid(form)

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all().order_by('datedebut')
    serializer_class = AlbumSerializer


