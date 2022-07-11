from django.shortcuts import render
from django.http import JsonResponse
import time

from events.forms import EventUserForm
from events.models import Event, EventUser

def index(request):
    # for this demo hardcoding a single event, but this could be extended to multiple event options
    event = Event.objects.get_or_create(name='My first festival', number_of_places=5)[0]
    
    if request.method == 'POST':
        time.sleep(1) # delay to see button disable while awaiting response
        form = EventUserForm(request.POST, event=event)
        if form.is_valid():
            username = form.cleaned_data['name']
            EventUser.objects.create(name=username, event=event)
            context = {
                'users': event.users.all(),
            }
            return render(request, 'events/partials/userlist.html', context)
        # if form has errors (over-subscribed event) return the form with errors displayed
        context = {'form': form}
        response = render(request, 'events/partials/form.html', context)
        # change HTMX target server-side from the userlist to the form itself
        response['HX-Retarget'] = '#submit-form'
        return response
    
    # if GET, load empty form
    context = {
            'event': event, 
            'form': EventUserForm(),
            'users': event.users.all(),
        }
    return render(request, 'events/index.html', context)

def check_spaces(request):
    # only one event in this demo app
    event = Event.objects.get(name='My first festival')
    spaces_available = event.users.count() < event.number_of_places
    return JsonResponse({'available': spaces_available})