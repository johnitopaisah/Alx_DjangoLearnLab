from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import CustomUser

# serializers.CharField()
User = get_user_model()
class CustomUserSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_pic', 'followers', 'following']

    
    
class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(min_length=8, write_only=True)
    # confirm_password = serializers.CharField(min_length=8, write_only=True)

    # class Meta:
    #     model = get_user_model()
    #     fields = ['username', 'email', 'password',]

    def validate_password(self, value):
        validate_password(value)
        return value

        
    def create(self, validated_data):
        try:
            user_data = {
                'username' : validated_data['username'],
                'email' : validated_data['email'],
                'password' : validated_data['password'],
            }
            user = User.objects.create_user(**user_data)
            token, _ = Token.objects.get_or_create(user=user)
            return {'username': user.username, 'token': token.key}
        except Exception as e:
            raise serializers.ValidationError(str(e))

    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError({'detail': "Invalid Credentials"})
        token, created = Token.objects.get_or_create(user=user)

        return {'username': user.username, 'token': token.key}
        
        # return Response({'username': user.username, 'token': token.key})
    
