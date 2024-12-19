from django import forms
from .models import lead

class LeadModelform(forms.ModelForm):
    class Meta:
        model = lead
        fields =(
            'first_name',
            'last_name',
            'age',
            'agent',
        )
class LeadForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    age = forms.IntegerField(min_value=0)