from django.shortcuts import render
from django.http import HttpResponse

def all_chai(request):
    return render(request, 'all_chai/index.html') 
