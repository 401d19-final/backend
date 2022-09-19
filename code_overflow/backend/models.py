from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField("Title",max_length = 128)
    content = models.TextField("Content")
    created_time = models.DateTimeField("Time_created",auto_now_add=True)
    updated_time = models.DateTimeField("Time_updated", auto_now=True)


    def __str__(self):
        return self.title

