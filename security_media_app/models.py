from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import uuid


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)


class FileBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Governorate(models.Model):
    idG = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class MediMessages(models.Model):
   id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
   # msg_id = models.AutoField(primary_key=True)
   msg_user = models.CharField(max_length=200)
   msg_title = models.CharField(max_length=200)
   msg_date = models.DateField(auto_now=True)
   msg_time = models.TimeField(auto_now=True)
   msg_content = models.CharField(max_length=1000)
   msg_governorate = models.ForeignKey(Governorate, on_delete=models.CASCADE)
   msg_fileBook = models.ForeignKey(FileBook, on_delete=models.CASCADE)
   msg_jih = models.CharField(max_length=300)
   msg_procedures = models.CharField(max_length=1000)
   msg_newseditor = models.CharField(max_length=200)
   msg_editdate = models.DateField(auto_now=True)
   msg_receiveteam = models.BooleanField(default=False)
   msg_secretary = models.BooleanField(default=False)
   msg_Minister = models.BooleanField(default=False)
   msg_published = models.BooleanField(default=False)
   msg_tracking = models.BooleanField(default=False)
   created_at = models.DateTimeField(auto_now=True)
   created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

   def __str__(self):
       return self.msg_title


class MediaAtt(models.Model):
    idattch = models.UUIDField(default=uuid.uuid4, editable=False)
    id_relt = models.ForeignKey('MediMessages', db_column='id_relt_id' ,on_delete=models.CASCADE)
    attch_title = models.CharField(max_length=300)
    attch_path = models.CharField(max_length=1000)

    def __str__(self):
        return self.attch_title


class MediaIfad(models.Model):

    idifada = models.UUIDField(default=uuid.uuid4, editable=False)
    id_relb = models.ForeignKey('MediMessages', db_column='id_relb_id' , on_delete=models.CASCADE)
    # id_relb = models.ForeignKey(MediMessages, related_name="Media_relation2", on_delete=models.CASCADE)
    ifada_title = models.CharField(max_length=300)
    ifada_path = models.CharField(max_length=1000)

    def __str__(self):
        return self.ifada_title
