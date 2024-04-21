from django.urls import path
from .views import show_vendors, delete_vendor, add_vendor, update_vendor, show_cust, add_cust, update_cust, delete_cust, adminDashboard, show_books

app_name='adminPanel'
urlpatterns = [
    # path('index/', index, name='index'),
    path('dashboard/', adminDashboard, name='dashboard'),
    path('show_vendors/', show_vendors, name='show_vendors'),
    path('add_vendor/', add_vendor, name='add_vendor'),
    path('update_vendor/<int:id>/', update_vendor, name='update_vendor'),
    path('delete_vendor/<int:id>/', delete_vendor, name='delete_vendor'),
    path('show_cust/', show_cust, name='show_cust'),
    path('add_cust/', add_cust, name='add_cust'),
    path('update_cust/<int:id>/', update_cust, name= 'update_cust'),
    path('delete_cust/<int:id>', delete_cust, name= 'delete_cust'),
    path('show_books/', show_books, name='show_books'),
    ]
