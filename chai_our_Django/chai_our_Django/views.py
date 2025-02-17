from django.shortcuts import render


from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello, Django!")
    return render (request, 'website/index.html')

def about(request):
    # return HttpResponse("About Us")
    return render (request, 'website/about.html')
def contact(request):
    # return HttpResponse("Contact Us")
    return render (request, 'website/contact.html')