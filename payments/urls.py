from django.urls import path
from .views import khalti

app_name = 'payments'
urlpatterns = [
    path('api/khalti_payment/', khalti, name='khalti')
]