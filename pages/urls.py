from django.urls import path ,include
from pages import views


urlpatterns = [
    path('',views.pages,name='home'),
    path('about/',views.about,name='about'),
    path('patient/',views.patient,name='patient'),
    path('patient registration/',views.patient_registration,name='registration_'),
   
]