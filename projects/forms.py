from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):

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
        model = Project
        widgets = {
            'name': forms.HiddenInput(),
            'cw_id': forms.HiddenInput(),
            'languages': forms.HiddenInput(),
            'description': forms.HiddenInput(),
            'tags': forms.HiddenInput(),
            'rank': forms.HiddenInput(),
            'url': forms.HiddenInput(),
        }