from django.urls import path, include
from ToDoApp import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


app_name = 'ToDoApp'
urlpatterns = [

    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='ToDoApp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='ToDoApp/index.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/password/', views.edit_password, name='edit_password'),


    # path('profile/password_reset/', password_reset, name='password_reset'),
    # path('profile/password_reset_done', password_reset_done, name='password_reset_done')
    # path('profile/password_reset', PasswordResetView.as_view(), name='password_reset'),
    # path('profile/password-reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('profile/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('profile/reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
