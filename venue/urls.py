from django.urls import path
from .views import home, vendor, contactus, payment, explore, partData

app_name = 'venue'
urlpatterns = [
    path('', home, name='home'),
    path('vendor/',vendor, name='vendor'),
    path('contactus/',contactus, name='contactus'),
    path('payment/',payment, name='payment'),
    path('explore/',explore, name='explore'),
    path('venue/<int:id>',partData, name='partData'),
    # path('venue/',show_venue, name='venues'),

]