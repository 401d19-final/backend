from django.urls import path
from .views import PostList, PostDetail, UserCreate, UserDelete

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("create/", UserCreate.as_view(), name="user_create"),
    path("/delete/<int:pk>", UserDelete.as_view(), name="user_delete")
]