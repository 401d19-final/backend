from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, DestroyAPIView
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserCreate(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or no users can register
    ]
    serializer_class = UserSerializer

class UserDelete(DestroyAPIView):
    pass
    # queryset = get_user_model()
    # serializer_class = UserSerializer
    # permission_classes=[]
    # def perform_destroy(self, instance):
    #     instance.delete_flag=True
    #     instance.save()

