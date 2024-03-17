from django import forms
from user.models import UserVendor

class VendorForm(forms.ModelForm):
    class Meta:
        model = UserVendor
        fields = ['username', 'name', 'email', 'password', 'phone', 'address']
        