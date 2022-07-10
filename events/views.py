from django.shortcuts import render

from events.forms import EventUserForm
from events.models import Event

def index(request):
    event = Event.objects.get_or_create(name='My first festival', number_of_places=5)[0]
    context = {'event': event, 'form': EventUserForm()}
    return render(request, 'events/index.html', context)

