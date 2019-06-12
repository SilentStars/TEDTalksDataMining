from .models import Movie,User
from .background import getUrl
from .background import video_recommendation,tagManage
from django.shortcuts import render
from .forms import RegisterForm

thismovietag = ['china', 'history']

def index(request): #recommendation part
    global thismovietag
    if request.method == 'POST': #选择后
        current_user_tag = request.user.tag
        current_user_id = request.user.id
        if  request.POST.get("pre") == 'like':  #like
            print("this movie tag test->")
            print(thismovietag)
            tags = tagManage.add(current_user_tag,thismovietag)
            print(tags)
            print("进行推荐用的tag《-")
            User.objects.filter(id=current_user_id).update(tag = tags) #把当前用户喜欢的tag更新
            csv_url,nextmovietag = video_recommendation.video_recommendation(tags) #获得当前视频的主页和标签，从csv来
            thismovietag[:] = nextmovietag
            print(thismovietag)
            print("这是我修改过后的<-")
            first_movie = getUrl.getUrl(csv_url)#获得下一个视频的url
            context = {'first_movie': first_movie}
            return render(request, 'polls/index.html', context)
        else:  #dislike
            print("this movie tag test->")
            print(thismovietag)
            tags = tagManage.delete(current_user_tag, thismovietag)
            print(tags)
            print("进行推荐用的tag《-")
            User.objects.filter(id=current_user_id).update(tag=tags)  # 把当前用户喜欢的tag更新
            csv_url, nextmovietag = video_recommendation.video_recommendation(tags)  # 获得当前视频的主页和标签，从csv来
            thismovietag[:] = nextmovietag
            first_movie = getUrl.getUrl(csv_url)  # 获得下一个视频的url
            context = {'first_movie': first_movie}
            return render(request, 'polls/index.html', context)
    else:#第一次访问
        first_movie_url = Movie.objects.get(id = 2)
        first_movie = getUrl.getUrl(first_movie_url)
        context = {'first_movie' : first_movie }
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

def register(request): #登录的提交

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