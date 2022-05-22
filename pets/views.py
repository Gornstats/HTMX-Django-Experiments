from django.shortcuts import render
from pets.models import Pet

# Create your views here.
def pet_list(request):
    pets = Pet.objects.all()
    context = {'pets': pets,}
    
    return render(request, 'pets/pet_list.html', context)
