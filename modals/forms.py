from django import forms
from modals.models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message', 'email']
        labels = {
            'message': 'Feedback',
        }
