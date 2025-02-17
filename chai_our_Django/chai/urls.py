
from django.urls import path
from . import views

# locahHost = 8000/chai 

urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    
    
]
