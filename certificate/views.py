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
    
    # simple example of a server side check to see if the date is valid 
    if 1970 <= int(date) <= 2050:
        return HttpResponse(date)
    else:
        return HttpResponse()

def edit_sign(request):
    sign = escape(request.POST.get('signature','')) 
    return HttpResponse(sign)

def generate_pdf(request):
    name = escape(request.POST.get('name','')) 
    qual = escape(request.POST.get('qual',''))
    date = escape(request.POST.get('awardDate',''))
    sign = escape(request.POST.get('signature',''))
    
    return HttpResponse("abcd")
    