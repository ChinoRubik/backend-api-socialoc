from django.db import models
from django.db.models import CASCADE
from users.models import User
import uuid

class Post(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=CASCADE)
    caption = models.TextField()
    # tagged = 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)