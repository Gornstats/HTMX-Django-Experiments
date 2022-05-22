from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http.response import HttpResponse
from django_htmx.http import trigger_client_event

from pets.models import Pet

def pet_list(request):
    pets = Pet.objects.all()
    context = {'pets': pets,}
    
    return render(request, 'pets/pet_list.html', context)

@require_http_methods(['POST'])
def add_pet(request):
    new_name = request.POST.get('petName','petNameError')
    if len(new_name) > 0:
        pet = Pet.objects.create(
            pet_name = new_name
        )
        pet_count = Pet.objects.count()
        context = {'pet': pet, 'pet_count': pet_count,}
    
        response = render(request, 'pets/partials/pet_li.html', context)
        trigger_client_event(response, 'pet_added', {})
        return response
    
    return HttpResponse(status=204)

def pet_alert(request):
    return render(request, 'pets/partials/pet_added.html', {})

def pet_alert_blank(request):
    return render(request, 'pets/partials/pet_added_blank.html', {})