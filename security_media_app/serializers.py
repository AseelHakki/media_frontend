
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.conf import settings
from .models import Department, FileBook, Governorate, MediMessages, MediaAtt, MediaIfad



class DepartmentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Department
       fields = "__all__"


class FileBookSerializer(serializers.ModelSerializer):
   class Meta:
       model = FileBook
       fields = "__all__"


class GovernorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governorate
        fields = "__all__"


class MediaAttSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAtt
        fields = "__all__"


class MediaIfadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaIfad
        fields = "__all__"


class MediMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediMessages
        fields = ('id', 'msg_user', 'msg_title', 'msg_date', 'msg_time','msg_content' ,'msg_governorate',
                    'msg_fileBook', 'msg_jih', 'msg_receiveteam', 'msg_secretary', 'msg_Minister', 'msg_published')


class MMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediMessages
        fields = ('id', 'msg_user', 'msg_title', 'msg_date', 'msg_time', 'msg_content', 'msg_governorate',
                  'msg_fileBook', 'msg_jih','msg_procedures', 'msg_receiveteam', 'msg_secretary', 'msg_Minister',
                  'msg_published', 'msg_newseditor', 'msg_editdate', 'msg_tracking')














# class UserSerializer(serializers.ModelSerializer):
   # class Meta:
   #
   #     model = User
   #
   #     fields = ('username', 'email', 'password')
   #
   #     extra_kwargs = {'password': {'write_only': True}}
   # def create(self, validated_data):
   #     user = User(email=validated_data['email'], username=validated_data['username'])
   #     user.set_password(validated_data['password'])
   #      user.save()
   #     Token.objects.create(user=user)
   #     return user


# class BookSerializer(serializers.ModelSerializer):
#
#    # author_username = serializers.CharField(source='author.username')
#
#
#    class Meta:
#
#        model = Book
#
#        fields = "__all__"


# class AuthorSerializer(serializers.ModelSerializer):
#
#    class Meta:
#
#        model = Author
#
#        fields = "__all__"



