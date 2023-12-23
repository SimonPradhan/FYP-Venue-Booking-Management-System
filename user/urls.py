from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('login_user/',views.login_user, name='login'),
    path('signup_user/',views.signup_user, name='signup'),
    path('logout_user/',views.logoutUser, name='logout'),
]