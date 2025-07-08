from django.urls import path
from .views import khalti, initiate_payment, invoice

app_name = 'payments'
urlpatterns = [
    path('api/khalti_payment/', khalti, name='khalti'),
    path('api/initiate_payment/', initiate_payment, name='initiate_payment'),
    path('invoice/', invoice, name='invoice')
]