from django.shortcuts import render
from .models import Description

def index(request):
   
    return render(request, 'core/index.html', {})

def gallery(request):
    
    descriptionObjects = Description.objects.all
    return render(request,'core/gallery.html', {'description': descriptionObjects})