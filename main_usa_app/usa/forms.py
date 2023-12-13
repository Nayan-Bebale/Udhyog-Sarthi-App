from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'job_title',
            'location',
            'job_type',
            'mode',
            'time',
            'categories',
            'salary',
            'hours',
            'about',
            'day_ago',
            'image',
        ]

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        # You can customize the form fields if needed
        # For example, add CSS classes or change widget attributes
        self.fields['about'].widget = forms.Textarea(attrs={'rows': 4})