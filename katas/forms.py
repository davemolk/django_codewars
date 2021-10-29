from django import forms

from .models import Exercise


class KataAPIForm(forms.ModelForm):

    class Meta:
        fields = [
            'name', 
            'cw_id', 
            'languages',
            'description',
            'tags',
            'rank',
            'url',
        ]
        model = Exercise
        widgets = {
            'name': forms.HiddenInput(),
            'cw_id': forms.HiddenInput(),
            'languages': forms.HiddenInput(),
            'description': forms.HiddenInput(),
            'tags': forms.HiddenInput(),
            'rank': forms.HiddenInput(),
            'url': forms.HiddenInput(),
        }