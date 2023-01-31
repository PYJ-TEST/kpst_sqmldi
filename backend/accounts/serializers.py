from rest_framework import serializers
from .models import User

class LoginSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(write_only=True)
    user_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'user_password']