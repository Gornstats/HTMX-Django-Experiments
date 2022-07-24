from django import forms
from modals.models import Feedback

class FeedbackForm(forms.ModelForm):
    
    def clean_email(self):
        email = self.cleaned_data['email']
        return email
        
    class Meta:
        model = Feedback
        fields = ['message', 'email']
        labels = {
            'message': 'Feedback',
        }
