from django.shortcuts import render
from .models import Image,Location

# Create your views here.
    # date = dt.date.today()
    # news = Article.todays_news()
    # return render(request, 'all-news/today-news.html', {"date": date,"news":news})

def index(request):
    images = Image.images()
    locations = Location.location()
    return render(request,'index.html', {"images": images[::1],"locations":locations})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})

def image_location(request,location):
    images = Image.filter_by_location(location)

    return render(request,'location.html',{"images":images})