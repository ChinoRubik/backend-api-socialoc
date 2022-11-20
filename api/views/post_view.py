from rest_framework.views import APIView
from rest_framework import status
from posts.models import Post
from api.serializers.post_serializer import PostSerializer
from api.serializers.image_serializer import ImageSerializer
from rest_framework.response import Response

class PostApiView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(status = status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer_post = PostSerializer(data=request.data)
        if (serializer_post.is_valid(raise_exception=True)):
            serializer_post.save()
            print(serializer_post,'fndsjahfhjksdaghfhkjsahfdjsaghf')
            request.data['post'] = serializer_post.data['uuid']
            serializer_image = ImageSerializer(data=request.data)
            if serializer_image.is_valid(raise_exception=True):
                serializer_image.save()
                return Response(serializer_image.data)