from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('login_user/',views.login_user, name='login'),
    path('logout_user/',views.logoutUser, name='logout'),
]