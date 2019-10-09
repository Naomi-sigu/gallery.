from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

# Create your views here.
def welcome(request):
     images = Image.get_images()
     return render(request, 'home.html', {"images":images})