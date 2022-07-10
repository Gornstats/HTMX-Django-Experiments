from django.shortcuts import render

from events.forms import EventUserForm
from events.models import Event, EventUser

def index(request):
    # for this demo hardcoding a single event, but this could be extended to multiple event options
    event = Event.objects.get_or_create(name='My first festival', number_of_places=5)[0]
    
    if request.method == 'POST':
        form = EventUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            EventUser.objects.create(name=username, event=event)
            context = {
                'users': event.users.all(),
            }
            return render(request, 'events/partials/userlist.html', context)
    
    context = {
            'event': event, 
            'form': EventUserForm(),
            'users': event.users.all(),
        }
    return render(request, 'events/index.html', context)

