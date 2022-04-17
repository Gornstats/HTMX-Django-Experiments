from django.shortcuts import render

# Create your views here.
def pet_list(request):
    return render(request, 'pets/pet_list.html')
