from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Post

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    # def destroy(self, request):
    #     user = request.user
    #     return super(UserSerializer, self).destroy(request)

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", )