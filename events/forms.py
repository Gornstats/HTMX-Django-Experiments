from django import forms

class EventUserForm(forms.Form):
    name = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        # if event in the kwargs, then we are editing an existing event
        # pop it from kwargs dictionary
        if "event" in kwargs:
            self.event = kwargs.pop('event')
        super().__init__(*args, **kwargs)
    
    def clean(self):
        # check if event is already at capacity (greater than number_of_places)
        if self.event.users.count() >= self.event.number_of_places:
            raise forms.ValidationError('Event is at capacity')
        return super().clean()