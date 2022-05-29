from django.shortcuts import render

def index(request):
    return render(request, 'dropdowns/dropdowns.html')

def options(request):
    animal = request.GET.get('animal')
    context ={'animal': animal,}
    
    return render(request, 'dropdowns/options.html', context)