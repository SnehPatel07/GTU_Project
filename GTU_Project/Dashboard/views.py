from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Dashboard/index.html')

def about_us(request):
    return render(request, 'Dashboard/about_us.html', {'title': "About Us"})

def contact_us(request):
    return render(request, 'Dashboard/contact_us.html', {'title': "Contact Us"})