from django.urls import path
from .views import home

app_name = 'venue'
urlpatterns = [
    path('', home, name='home'),
]