from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('data/',views.data, name = 'data'),
    path('about/',views.about, name = 'about'),
    path('contact/',views.contact, name = 'contact'),
    path('home2/',views.home2, name = 'home2'),
    path('home3/',views.home3, name = 'home3'),
    path('register/',views.register , name = 'register'),
    path('signup/' , views.signup, name = 'signup')
]