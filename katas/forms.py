from django import forms

from .models import Exercise


class KataAPIForm(forms.ModelForm):

    class Meta:
        fields = [
            'name', 
            'cw_id', 
            'rank',
            'tags',
            'url',
            'languages',
            'description',
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

class KataForm(forms.ModelForm):

    class Meta:
        fields = [
            'name', 
            'cw_id', 
            'rank',
            'tags',
            'url',
            'languages',
            'description',
            'notes',
        ]
        model = Exercise