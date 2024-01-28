from django import forms
from usa.models import Job, Courses, Lecture, DisabilityType, Companies
from ckeditor.widgets import CKEditorWidget

class JobForm(forms.ModelForm):
    about = forms.CharField(required=False, widget=forms.Textarea)
    distypes = forms.ModelMultipleChoiceField(
        queryset=DisabilityType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Job
        fields = ['job_title', 'location', 'job_type', 'mode', 'time', 'categories', 'salary', 'hours', 'about', 'last_date', 'is_published', 'distypes']

class CompanyForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea)
    class Meta:
        model = Companies
        fields = ['name', 'description', 'industry_type', 'logo', 'url']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['title', 'description', 'instructor', 'disability_types', 'courseimg']

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'video_url', 'description', 'sequence_order']