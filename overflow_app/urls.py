from django.urls import path
from .views import QuestionList, QuestionDetail, UserCreate, CommentList, CommentDetail,UserDetail

urlpatterns = [
    #CRUD Qeustion
    #GET all question, CREATE a new question
    path("question", QuestionList.as_view(), name="post_list"),
    #UPDATE, DELETE a question using question's primary key
    path("question/<int:pk>/", QuestionDetail.as_view(), name="post_detail"),


    #CRUD Comment
    #GET, UPDATE, DELETE a comment using comment's primary key
    path("comment/<int:pk>/", CommentDetail.as_view()),
    #GET all Comments for a specific Question
    path("question/<int:pk>/comment", CommentList.as_view()),


    #CRUD USER
    #CREATE a new user
    path("user/create/", UserCreate.as_view()),
    #GET, UPDATE, DELETE a user
    path("user/<int:pk>", UserDetail.as_view())
]