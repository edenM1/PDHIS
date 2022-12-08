
from django.contrib import admin
from django.urls import path ,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('pages.urls')),
    path('registration/',include('users.urls')),
    path('patient/',include('pages.urls')),
    path('patient_registration/',include('pages.urls')),
    path('about/',include('pages.urls')),
    

]
