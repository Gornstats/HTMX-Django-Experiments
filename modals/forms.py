from django import forms
from modals.models import Feedback

class FeedbackForm(forms.ModelForm):
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if email.startswith('c'):
            raise forms.ValidationError("Email can't start with c")
        return email
        
    class Meta:
        model = Feedback
        fields = ['message', 'email']
        labels = {
            'message': 'Feedback',
        }
