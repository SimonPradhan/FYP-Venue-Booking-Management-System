from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class UserCustSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustomer
        fields = ('id', 'username', 'email')

class UserVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVendor
        fields = ('id', 'username', 'email', 'name')