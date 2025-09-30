from django import forms
from .models import Youth, YouthActivity

class YouthForm(forms.ModelForm):
    class Meta:
        model = Youth
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'status', 'registration_due']

# Form for youth activities can be added similarly
class YouthActivityForm(forms.ModelForm):
    class Meta:
        model = YouthActivity
        fields = ['youth', 'activity', 'participation_date', 'notes', 'result']