from rest_framework import serializers
from .models import Question, Comment
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Question

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", "email")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Comment