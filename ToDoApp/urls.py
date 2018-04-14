from django.urls import path
from ToDoApp import views
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done
)


app_name = 'ToDoApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', login, {'template_name':'ToDoApp/login.html'} ,name='login'),
    path('logout/', logout, {'template_name':'ToDoApp/index.html'} ,name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/password/', views.edit_password, name='edit_password'),
    path('profile/password_reset/', password_reset, name='password_reset'),
    path('profile/password_reset_done', password_reset_done, name='password_reset_done')
]
