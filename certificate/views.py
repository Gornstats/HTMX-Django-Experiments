from django.shortcuts import render

# Create your views here.
def certificate_builder(request):
    return render(request, "certificate/certificate.html")