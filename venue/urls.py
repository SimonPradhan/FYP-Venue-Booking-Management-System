from django.urls import path
from .views import home, contactus, payment, explore, partData, gallery, booking

app_name = 'venue'
urlpatterns = [
    path('', home, name='home'),
    path('contactus/',contactus, name='contactus'),
    path('payment/',payment, name='payment'),
    path('explore/',explore, name='explore'),
    path('venue/<int:id>',partData, name='partData'),
    # path('venue/',show_venue, name='venues'),
    path('booking/',booking, name='booking'),
    path('gallery/', gallery, name='gallery')
    ]