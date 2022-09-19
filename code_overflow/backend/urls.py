from django.urls import path
from .views import QuestionList, QuestionDetail, UserCreate, CommentList, CommentDetail

urlpatterns = [
    path("question", QuestionList.as_view(), name="post_list"),
    path("question/<int:pk>/", QuestionDetail.as_view(), name="post_detail"),
    path("comment", CommentList.as_view()),
    #Change this to foreign key to get all comments with specific question
    path("comment/<int:pk>", CommentDetail.as_view()),

    path("create/", UserCreate.as_view(), name="user_create"),

]