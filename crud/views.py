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
    
    return render(request, 'crud/partials/person.html', {'person': person, 'adding_new_client': False})

@require_http_methods(['GET'])
def create_person(request):
    
    return render(request, 'crud/partials/create_person.html')

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
    
    return render(request, 'crud/partials/person.html', {'person': person, 'adding_new_client': False})

@require_http_methods(['POST'])
def create(request):
    person = Person.objects.create(
        first_name=request.POST.get('firstName','firstnameError'),
        last_name=request.POST.get('lastName','secondnameError'),
        email_address=request.POST.get('email','emailError')
    )
    
    return render(request, 'crud/partials/person.html', {'person': person, 'adding_new_client': True})

@require_http_methods(['GET'])
def cancel_create(request):
    
    return render(request, 'crud/partials/create_button.html')
