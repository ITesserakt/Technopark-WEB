from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hot', views.hot, name='hot'),
    path('ask', views.ask, name='ask'),
    path('tag/<str:tag_name>', views.tag, name='tag'),
    path('settings', views.settings, name='settings'),
    path('login', views.login, name='login'),
    path('singup', views.register, name='register'),
    path('question/<int:question_id>', views.question, name='question')
]