# forms.py
from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('user','violation_date', 'place', 'district', 'state', 'uploaded_file','comment')

    uploaded_file = forms.FileField(label='Uploaded File', required=False, widget=forms.ClearableFileInput(attrs={'multiple': False}))

    def clean_uploaded_file(self):
        uploaded_file = self.cleaned_data.get('uploaded_file')

        # You can add custom validation for the file if needed
        # For example, check the file type or size

        return uploaded_file
