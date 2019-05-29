from .models import Movie
from .background import getUrl
from .background import video_recommendation
from django.shortcuts import render
from .forms import RegisterForm

def index(request): #recommendation part
    tags = "culture,friendship,history"
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

def register(request): #注册和登录的提交

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_movie_url = Movie.objects.get(id=1)
            first_movie = getUrl.getUrl(first_movie_url)
            context = {'first_movie': first_movie}
            return render(request,'polls/index.html',context)

    else:
        form = RegisterForm()
    return render(request, 'polls/register.html',context={'form': form})

def signup(request):#注册界面
    return render(request,'polls/register.html')

def sample_view(request):
    current_user = request.user
    print(current_user.id)