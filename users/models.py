from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid

class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, null=False, default='H')
    date_birthday = models.DateField(null=True)

    #TO LOG IN IN ADMIN AS EMAIL
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
