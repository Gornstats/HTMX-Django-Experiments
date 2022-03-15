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

@require_http_methods(['POST'])
def update_person(request, pk):
    person = Person.objects.get(pk=pk)

    person.first_name = request.POST.get('firstName','firstnameError')
    person.last_name = request.POST.get('lastName','secondnameError')
    person.email_address = request.POST.get('email','emailError')
    person.save()
    
    return render(request, 'crud/partials/person.html', {'person': person})
