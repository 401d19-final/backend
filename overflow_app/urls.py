from django.urls import path
from .views import QuestionList, QuestionDetail, UserCreate, CommentList, CommentDetail

urlpatterns = [
    #CRUD Qeustion
    path("question", QuestionList.as_view(), name="post_list"),
    path("question/<int:pk>/", QuestionDetail.as_view(), name="post_detail"),
    #CRUD Comment
    path("comment/<int:pk>/", CommentDetail.as_view()),
    path("question/<int:pk>/comment", CommentList.as_view()),
    #Create a new user
    path("create/", UserCreate.as_view(), name="user_create"),

]