from django import forms
from django.core.exceptions import ValidationError
from django.forms import CharField, ModelForm, inlineformset_factory
from requisition.models import *


class RequisitionForm(ModelForm):
    class Meta:
        model = Requistion
        fields = '__all__'
        # exclude = ('evenement','user')
        widgets = {
            # 'description': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
            'commentaire': forms.Textarea(attrs={'cols': 50, 'rows': 3}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_demande'].widget.attrs.update({
            'id': 'datedebut'
        })
        '''self.fields['description'].widget.attrs.update({
            'placeholder':'1 VP - VGP"'
        })'''


class RequerantForm(ModelForm):
    class Meta:
        model = Requerant
        fields = '__all__'
