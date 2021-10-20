from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ask', views.ask, name='ask'),
    path('tag', views.tag, name='tag'),
    path('settings', views.settings, name='settings'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('question', views.question, name='question')
]