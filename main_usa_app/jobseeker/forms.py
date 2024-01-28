from django import forms
from usa.models import Applicant

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'email', 'resume']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'resume': forms.FileInput(attrs={'class': 'form-control bg-white'}),
        }
