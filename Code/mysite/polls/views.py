from .models import Movie,User
from .background import getUrl
from .background import video_recommendation,tagManage,regression
from django.shortcuts import render
from .forms import RegisterForm
import random

thismovietag = ['china', 'history']

def index(request): #recommendation part
    global thismovietag
    if request.method == 'POST': #选择后
        current_user_tag = request.user.tag
        current_user_id = request.user.id
        if  request.POST.get("pre") == 'like':  #like
            tags = tagManage.add(current_user_tag,thismovietag)
            User.objects.filter(id=current_user_id).update(tag = tags) #把当前用户喜欢的tag更新
            csv_url,nextmovietag = video_recommendation.video_recommendation(tags) #获得当前视频的主页和标签，从csv来
            thismovietag[:] = nextmovietag
            first_movie = getUrl.getUrl(csv_url)#获得下一个视频的url
            context = {'first_movie': first_movie}
            return render(request, 'polls/index.html', context)
        else:  #dislike

            tags = tagManage.delete(current_user_tag, thismovietag)
            User.objects.filter(id=current_user_id).update(tag=tags)  # 把当前用户喜欢的tag更新
            csv_url, nextmovietag = video_recommendation.video_recommendation(tags)  # 获得当前视频的主页和标签，从csv来
            thismovietag[:] = nextmovietag
            first_movie = getUrl.getUrl(csv_url)  # 获得下一个视频的url
            context = {'first_movie': first_movie}
            return render(request, 'polls/index.html', context)
    else:#第一次访问
        number = random.randint(2, 40)
        first_movie_url = Movie.objects.get(id = number)
        first_movie = getUrl.getUrl(first_movie_url)
        context = {'first_movie' : first_movie }
        return render(request, 'polls/index.html', context)

def data(request):
    if request.method == 'GET':
        return render(request, 'polls/trailor.html')
    else:
        min = request.POST.get('name1', None)
        second = request.POST.get('name2', None)
        language = request.POST.get('name3', None)
        views = request.POST.get('name4', None)
        year = request.POST.get('name5', None)
        month = request.POST.get('name6', None)
        day = request.POST.get('name7', None)
        number = regression.regression_predict(min,second,language,views,year,month,day)
        context = {'number': number}
        return render(request, 'polls/trailor.html',context)



def about(request):
    return render(request,'polls/about.html')

def contact(request):
    return render(request,'polls/contact.html')

def home2(request):
    return render(request,'polls/index-3.html')

def home3(request):
    return render(request,'polls/index-4.html')

def register(request): #登录的提交

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            number2 = random.randint(5, 40)
            form.save()
            first_movie_url = Movie.objects.get(id=number2)
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