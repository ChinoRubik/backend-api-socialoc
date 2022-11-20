from rest_framework import serializers
from posts.models import Post
from images.models import Image

class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = ['uuid', 'user', 'caption', 'created_at', 'updated_at']
