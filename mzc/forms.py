from django import forms
from .models import faculity
class FaculityForm(forms.ModelForm):
    class Meta:
        model=faculity
        fields='__all__'