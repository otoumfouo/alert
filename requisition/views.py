from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from requisition.models import *
from requisition.forms import *
# Create your views here.
# Create your views here.
@login_required
def index(request):
    requistionList = Requistion.objects.all().order_by('created_at')
    return render(request, 'requisition/index.html', locals())


@login_required
def requistionList(request):
    alerts = Alert.objects.all().order_by('datedebut')
    return render(request, 'index.html', locals())


@login_required
def create(request):
    form = RequisitionForm(request.POST or None, request.FILES or None)
    if request.POST :
        if form.is_valid() :
            form.save()
    return render(request, 'requisition/form.html', locals())


@login_required
def rapportRequisitionList(request):
    alerts = Alert.objects.all().order_by('datedebut')
    return render(request, 'index.html', locals())

