from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from crud.models import Person

# Create your views here.
def live_edit(request):
    people = Person.objects.all()
    
    return render(request, 'crud/live_edit.html', {'people': people})

@require_http_methods(['GET'])
def get_person(request, pk):
    person = Person.objects.get(pk=pk)
    
    return render(request, 'crud/partials/person.html', {'person': person})

@require_http_methods(['GET'])
def edit_person(request, pk):
    person = Person.objects.get(pk=pk)
    
    return render(request, 'crud/partials/editable.html', {'person': person})

@require_http_methods(['PUT'])
def update_person(request, pk):
    person = Person.objects.get(pk=pk)
    
    person.first_name = request.PUT['firstName']
    person.last_name = request.PUT['lastName']
    person.email_address = request.PUT['email']
    person.save()
    
    return render(request, 'crud/partials/person.html', {'person': person})
