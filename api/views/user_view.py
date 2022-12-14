from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.user_serializer import UserRegisterSerializer
from rest_framework import status

class RegisterView(APIView):
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
