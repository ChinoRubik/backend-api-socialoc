from django.db import models
from posts.models import Post
from django.db.models import CASCADE
import uuid

class Image(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=CASCADE)
    image = models.ImageField(upload_to='media/')
