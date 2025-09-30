from django import forms
from .models import Youth, YouthActivity, Activity

class YouthForm(forms.ModelForm):
    class Meta:
        model = Youth
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'status', 'registration_due']

# activity form can be added similarly
class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_name', 'description', 'start_date', 'end_date', 'location']


# Form for youth activities can be added similarly
class YouthActivityForm(forms.ModelForm):
    class Meta:
        model = YouthActivity
        fields = ['youth', 'activity', 'notes', 'result']