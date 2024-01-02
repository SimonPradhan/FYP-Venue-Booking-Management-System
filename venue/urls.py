from django.urls import path
from .views import home, vendor

app_name = 'venue'
urlpatterns = [
    path('', home, name='home'),
    path('vendor/',vendor, name='vendor'),
    # path('venue/',show_venue, name='venues'),

]