from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Movie
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .background import getUrl
from .background import video_recommendation

def index(request): #recommendation part
    tags = "culture,friendship,china"
    if request.method == 'POST':
        if  request.POST.get("pre") == 'like':  #like
            csv_url = video_recommendation.video_recommendation(tags)
            first_movie = getUrl.getUrl(csv_url)
            context = {'first_movie': first_movie}
            return render(request, 'polls/index.html', context)
        else:  #dislike
            csv_url = video_recommendation.video_recommendation(tags)
            first_movie = getUrl.getUrl(csv_url)
            context = {'first_movie': first_movie}
            return render(request, 'polls/index.html', context)
    else:
        first_movie_url = Movie.objects.get(id = 2)
        first_movie = getUrl.getUrl(first_movie_url)
        context = {'first_movie' : first_movie}
        return render(request, 'polls/index.html', context)

def data(request):
    return render(request,'polls/trailor.html')

def about(request):
    return render(request,'polls/about.html')

def contact(request):
    return render(request,'polls/contact.html')

def home2(request):
    return render(request,'polls/index-3.html')

def home3(request):
    return render(request,'polls/index-4.html')

def login(request):
    return render(request,'polls/login.html')

def register(request):
    return render(request,'polls/register.html')