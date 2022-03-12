from django.shortcuts import render

# Create your views here.
def live_edit(request):
    return render(request, 'crud/live_edit.html', {})
