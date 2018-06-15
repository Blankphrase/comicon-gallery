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

def search_results(request):
    '''
    Handles search requests
    Users input is used to search for images that much that description using inbuilt regex search
    renders the results with the following params: found photos, locations, categories
    '''
    if 'image' in request.GET and request.GET["image"]:
        query = request.GET.get("image")
        photos = Image.searched(query)
        message = f"{query}"

        return render(request, 'results.html',
                      {"message": message, "photos": photos,"locations":locations,"categories":categories})
    else:
        message = "What images do you want to search for?"
        return render(request, 'results.html',
                      {"message": message,"locations":locations,"categories":categories})






