from django.shortcuts import render
from crud.models import Person

# Create your views here.
def live_edit(request):
    people = Person.objects.all()
    
    return render(request, 'crud/live_edit.html', {'people': people})
