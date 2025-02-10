from django import forms
from aid_management.models import AidRecipients

class AidRecipientForm(forms.ModelForm):
    class Meta:
        model = AidRecipients
        fields = ['aid_status', 'aid_type', 'aid_desc', 'aid_startdate', 'aid_enddate']
        # You can customize widgets if needed (e.g., date pickers)
        widgets = {
            'aid_startdate': forms.DateInput(attrs={'type': 'date'}),
            'aid_enddate': forms.DateInput(attrs={'type': 'date'}),
        }