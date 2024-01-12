from django.contrib import admin
from django.urls import path
#
from security_media_app.apiviews import DepartmentAPI , FileBookAPI , MediaAttAPI , MediaIfadAPI , MMessagesAPI , MediMessagesAPI

from core.serializers import CustomUserSerializer
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
   def validate(self, attrs):
      data = super().validate(attrs)
      print(data)
      # Assuming you have a serializer for your user model
      user_serializer = CustomUserSerializer(self.user).data
      data.update({'user': user_serializer})
      return data


class CustomTokenObtainPairView(TokenObtainPairView):
   serializer_class = CustomTokenObtainPairSerializer

urlpatterns = [

   path('admin/', admin.site.urls),

  # path('login/', views.obtain_auth_token, name='login'),
  # path('users/', UsersList.as_view(), name="Users List"),
  # path('users/<int:pk>', UserDetails.as_view(), name="Users List"),
   path('DepartmentAPI/', DepartmentAPI.as_view(), name="All Records"),
   path('FileBookAPI/', FileBookAPI.as_view(), name="All Records"),
   path('MediaAttAPI/', MediaAttAPI.as_view(), name="All Records"),
   path('MMessagesAPI/', MMessagesAPI.as_view(), name="All Records"),
   path('MediaIfadAPI/', MediaIfadAPI.as_view(), name="All Records"),
   path('MediMessagesAPI/', MediMessagesAPI.as_view(), name="All Records"),
   # login
   path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
