from .models import Question, Comment
from .serializers import QuestionSerializer, UserSerializer, CommentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, DestroyAPIView, ListAPIView
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions

class QuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class CommentList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

#Remove
class UserList(ListCreateAPIView):
    queryset = get_user_model()
    serializer_class = UserSerializer

class UserCreate(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or no users can register
    ]
    serializer_class = UserSerializer

# class UserDelete(DestroyAPIView):
#     pass
#     # queryset = get_user_model()
#     # serializer_class = UserSerializer
#     # permission_classes=[]
#     # def perform_destroy(self, instance):
#     #     instance.delete_flag=True
#     #     instance.save()

