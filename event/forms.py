from django import forms
from django.core.exceptions import ValidationError
from django.forms import CharField, ModelForm, inlineformset_factory
from .models import *


class AlertsForm(ModelForm):
    class Meta:
        model = Alert
        fields = '__all__'
        exclude = ('evenement','user')
        widgets = {
            #'description': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
            'commentaire': forms.Textarea(attrs={'cols': 50, 'rows': 3}),

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['datedebut'].widget.attrs.update({
            'id': 'datedebut'
        })
        self.fields['description'].widget.attrs.update({
            'placeholder':'1 VP - VGP"'
        })


class degatForm(ModelForm):
    class Meta:
        model = Degats
        exclude = ("alert",)
        fields = '__all__'
        widgets = {
            # 'Value': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['type_degat'].label = ""
        #self.fields['nbre'].label = ""
        # self.fields['TypeInfo'] = forms.ModelChoiceField(queryset=TypeInfo.objects.all(),  empty_label="")

'''class Fichiers_alertForm(ModelForm):
    class Meta:
        model = Fichiers_alert
        exclude = ("alert",)
        fields = '__all__'
        widgets = {
            # 'Value': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)'''


AlertDegatFormSet = inlineformset_factory(Alert, Degats,
                                                 form=degatForm, can_delete=True, extra=2, fk_name="alert")

#AlertFichierFormSet = inlineformset_factory(Alert, Fichiers_alert, form=Fichiers_alertForm,can_delete=True, extra=2, fk_name="alert")


class EventForm(ModelForm):
    class Meta:
        model = Evenement
        fields = '__all__'
        '''widgets = {
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
        }'''
