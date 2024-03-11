from django.urls import path
from .views import index, show_vendors, delete_vendor

app_name='adminPanel'
urlpatterns = [
    path('index/', index, name='index'),
    path('show_vendors/', show_vendors, name='show_vendors'),
    path('delete_vendor/<int:id>/', delete_vendor, name='delete_vendor'),
    ]