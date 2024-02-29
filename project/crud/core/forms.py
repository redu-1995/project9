from django import forms
from .models import jobnew

class AddJobForm(forms.ModelForm):
    class Meta:
        model = jobnew
        fields = ('position','job_time','job_type','place_of_work','deadline')
        widgets = {
            'position': forms.TextInput(attrs={'class':'form-control'}),
            'job_time': forms.TextInput(attrs={'class':'form-control'}),
            'job_type': forms.TextInput(attrs={'class':'form-control'}),
            'place_of_work': forms.TextInput(attrs={'class':'form-control'}),
            'deadline': forms.TextInput(attrs={'class':'form-control'}),
        }