from django.shortcuts import render
from .models import About
from django.views import View

# Create your views here.

def about_me(request):
    
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )