from django.urls import path
from .views import vendor

app_name = 'vendor'
urlpatterns = [
    path('vendor/',vendor, name='vendor'),
]