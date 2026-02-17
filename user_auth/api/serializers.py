from django.contrib.auth.models import User
from rest_framework import serializers
from user_auth.models import UserProfile

class RegistrationSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    repeated_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['repeated_password']:
            raise serializers.ValidationError({'error': 'Passwords do not match'})
        return attrs

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exists')
        return value

    def save(self):
        data = self.validated_data
        fullname = data['fullname']
        username = fullname.replace(' ', '.')
        
        drf_user = User.objects.create_user(
            username=username,
            email=data['email'],
            password=data['password']
        )
        
        user_profile = UserProfile.objects.create(
            user=drf_user,
            fullname=data['fullname']
        )
        
        return drf_user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, request):
        email = request.get('email')
        password = request.get('password')

        if not email or not password:
            raise serializers.ValidationError('Email and password are required.')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid email or password.')

        if not user.check_password(password):
            raise serializers.ValidationError('Invalid email or password.')

        request['user'] = user
        return request

