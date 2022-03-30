from django.shortcuts import render, HttpResponse
from django.utils.html import escape

# Create your views here.
def certificate_builder(request):
    return render(request, "certificate/certificate.html")

def edit_name(request):
    name = escape(request.POST.get('name','')) 
    return HttpResponse(name)

def edit_qual(request):
    qual = escape(request.POST.get('qual',''))
    return HttpResponse(qual)

def edit_date(request):
    date = escape(request.POST.get('awardDate','')) 
    return HttpResponse(date)

def edit_sign(request):
    sign = escape(request.POST.get('signature','')) 
    return HttpResponse(sign)