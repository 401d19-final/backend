from .models import Question, Comment
from .serializers import QuestionSerializer, UserSerializer, CommentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, DestroyAPIView, ListAPIView
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions

class QuestionList(ListCreateAPIView):
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class CommentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentList(ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comment.objects.filter(question__id=self.kwargs['pk'])

class UserCreate(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or no users can register
    ]
    serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model()
    serializer_class = UserSerializer
