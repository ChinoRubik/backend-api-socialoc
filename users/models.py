from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid

class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, null=False, default='H')
    date_birthday = models.DateField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
