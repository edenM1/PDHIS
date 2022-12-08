from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def pages(request): # the url routing for the home page
    return render(request,'home.html',{'text':" "}) 

def patient(request): # the url routing for the patient page
    return render(request,'patient_page.html',{'text':""}) 

def about(request): # the url routing for the info page
    
    return render(request,'About_us.html',{'text':""}) 

def patient_registration(request):
    return render(request,'patient_registration.html',{'text':'registration'})