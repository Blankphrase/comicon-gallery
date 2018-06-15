from django.shortcuts import render
from .models import Image

global locations,categories
locations=["Metropolis","Gotham","Central City","Avengers mansion","Bifrost","Wakanda"]
categories=["Marvel","DC"]

def index(request):
    '''
    Handles requests for the homepage
    renders index.hmtl with the following params title, photos, locations and categories
    '''
    title = 'Welcome'
    photos = Image.get_all()
    return render(request, 'index.html',
                  {"title": title,
                   "photos": photos,
                   "locations":locations,
                   "categories":categories})


