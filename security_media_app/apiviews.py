from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from .models import Department, FileBook, Governorate, MediMessages, MediaAtt, MediaIfad
from .serializers import DepartmentSerializer, FileBookSerializer, GovernorateSerializer,\
                            MediaAttSerializer, MediaIfadSerializer, MediMessagesSerializer, MMessagesSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings


class DepartmentAPI(generics.ListCreateAPIView):
   queryset = Department.objects.all()
   serializer_class = DepartmentSerializer
   permission_classes = [IsAuthenticated, DjangoModelPermissions]


class FileBookAPI(generics.ListCreateAPIView):
   queryset = FileBook.objects.all()
   serializer_class = FileBookSerializer
   permission_classes = [IsAuthenticated, DjangoModelPermissions]


class GovernorateAPI(generics.ListCreateAPIView):
   queryset = Governorate.objects.all()
   serializer_class = GovernorateSerializer
   permission_classes = [IsAuthenticated, DjangoModelPermissions]


class MediaAttAPI(generics.ListCreateAPIView):
   queryset =MediaAtt.objects.all()
   serializer_class = MediaAttSerializer
   permission_classes = [IsAuthenticated, DjangoModelPermissions]


class MediaIfadAPI(generics.ListCreateAPIView):
   queryset =MediaIfad.objects.all()
   serializer_class =MediaIfadSerializer
   permission_classes = [IsAuthenticated, DjangoModelPermissions]


class MediMessagesAPI(generics.ListCreateAPIView):
   queryset = MediMessages.objects.all()
   serializer_class = MediMessagesSerializer
   permission_classes = [IsAuthenticated, DjangoModelPermissions]


class MMessagesAPI(generics.ListCreateAPIView):
   queryset = MediMessages.objects.all()
   serializer_class = MMessagesSerializer
   permission_classes = [IsAuthenticated, DjangoModelPermissions]

   # def get_queryset(self):
   #    # Get the current user from the request
   #    user = self.request.user
   #    if user.is_superuser:
   #       return MediMessagesAPI.objects.all()[:100]
   #    # Filter the queryset to return records created by this user
   #    return MediMessagesAPI.objects.filter(created_by=user)[:100]

