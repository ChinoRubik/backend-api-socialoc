from django.urls import path
from api.views.post_view import PostApiView

urlpatterns = [
    path('posts/', PostApiView.as_view(), name='posts')
]