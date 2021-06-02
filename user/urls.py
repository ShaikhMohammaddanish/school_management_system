
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.signout, name='signout'),
    path('profile', views.profile, name='profile'),
]
