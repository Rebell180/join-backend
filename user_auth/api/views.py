from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import os

from user_auth.api.serializers import RegistrationSerializer, LoginSerializer


# Create your views here.
class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            try:
                saved_account = serializer.save()
                token, created = Token.objects.get_or_create(user=saved_account)
                profile = saved_account.userprofile
                
                data = {
                    'token': token.key,
                    'fullname': profile.fullname,
                    'email': saved_account.email,
                    'user_id': saved_account.id
                }
                return Response(data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = serializer.validated_data['user']
                token, created = Token.objects.get_or_create(user=user)
                profile = user.userprofile
                
                data = {
                    'token': token.key,
                    'fullname': profile.fullname,
                    'email': user.email,
                    'user_id': user.id
                }
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginGuestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        guest_data = {
            'email' : os.getenv('GUEST_USER_EMAIL'),
            'password': os.getenv('GUEST_USER_PW')
        }
        serializer = LoginSerializer(data=guest_data)

        if serializer.is_valid():
            try:
                user = serializer.validated_data['user']
                token, created = Token.objects.get_or_create(user=user)
                profile = user.userprofile
                
                data = {
                    'token': token.key,
                    'fullname': profile.fullname,
                    'email': user.email,
                    'user_id': user.id
                }
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()  # Token löschen
        return Response({"detail": "Logout erfolgreich. Token wurde gelöscht."}, status=status.HTTP_200_OK)