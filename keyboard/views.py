from django.shortcuts import render

# Create your views here.
def button_press(request):
    return render(request, 'keyboard/button_press.html')
