from django.conf import settings
# from .models import User
from rest_framework import serializers
# from django.contrib.auth import get_user_model
# User = get_user_model()
from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
    # department = serializers.CharField(source='department.name')
    # directorate = serializers.CharField(source='directorate.name')
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'department']
