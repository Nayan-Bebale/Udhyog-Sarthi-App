from django import forms
from .models import Job, Courses, Lecture
from ckeditor.widgets import CKEditorWidget

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
            'disability_types',
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
        self.fields['about'].widget = CKEditorWidget()

class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['title', 'description', 'instructor', 'disability_types', 'courseimg']

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'video_url', 'description', 'sequence_order']