from django.db import models
from django.contrib.auth.models import AbstractUser
from security_media_app.models import Department


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    # department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)

