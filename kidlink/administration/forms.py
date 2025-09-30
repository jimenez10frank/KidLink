from django import forms
from .models import Youth

class YouthForm(forms.ModelForm):
    class Meta:
        model = Youth
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'status', 'registration_due']