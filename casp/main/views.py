from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def academics(request):
    return render(request, 'main/academics.html')

def admissions(request):
    return render(request, 'main/admissions.html')

def departments(request):
    return render(request, 'main/departments.html')

def placement(request):
    return render(request, 'main/placement.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def students_corner(request):
    return render(request, 'main/home.html')

def iqac(request):
    return render(request, 'main/home.html')

def contact(request):
    return render(request, 'main/contact.html')

def principal_message(request):
    return render(request, 'main/principal_message.html')