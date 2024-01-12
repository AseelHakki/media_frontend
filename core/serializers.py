from django.conf import settings
from rest_framework import serializers
from .models import User



class CustomUserSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.name')
    # directorate = serializers.CharField(source='directorate.name')
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'department']
