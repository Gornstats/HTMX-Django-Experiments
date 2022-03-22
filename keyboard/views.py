from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http.response import HttpResponse

# Create your views here.
def button_press(request):
    return render(request, 'keyboard/button_press.html')

@require_http_methods(['POST'])
def change_colour(request, colour):
    return HttpResponse("<div id='colourBox' style='background-color:" + colour + ";'></div>")
