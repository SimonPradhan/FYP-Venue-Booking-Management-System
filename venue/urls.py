from django.urls import path
from .views import home, vendor, contactus

app_name = 'venue'
urlpatterns = [
    path('', home, name='home'),
    path('vendor/',vendor, name='vendor'),
    path('contactus/',contactus, name='contactus')
    # path('venue/',show_venue, name='venues'),

]