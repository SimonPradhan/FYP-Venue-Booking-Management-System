from django.urls import path
from .views import vendor, details

app_name = 'vendor'
urlpatterns = [
    path('vendor/',vendor, name='vendor'),
    path('details/',details, name='details'),
]