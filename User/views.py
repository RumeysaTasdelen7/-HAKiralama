from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from User.models import CustomUser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import ChangePasswordSerializer, LoginSerializer, RegisterSerializer, CustomUserSerializer
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from core.page_filter import pages_filter
import math
# Create your views here.

class RegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Registration successfully done', 'success': True})
    

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        access_token = str(AccessToken.for_user(user))

        return Response({"token": access_token})
    

class UserListAPIView(ListAPIView):
    serializer_class = CustomUserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["firstName", "email"]


    def get_queryset(self):
        queryset = CustomUser.objects.all()

        if self.request.path == '/user/':
            return CustomUser.objects.filter(id=self.request.user.id)
        else:
            return queryset
        
    def list(self, request, *args, **kwargs):
        if request.path.startswith('/user/auth/pages/') or request.path.startswith('/user/auth/pages'):
            return pages_filter(self, request, CustomUser, *args, **kwargs)
        return super().list(request, *args, **kwargs)
    

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        data = super().update(request, *args, **kwargs)
        return Response({"update": "successful", "success": True})


# class UserListView(APIView):
#     def get(self, request, *args, **kwargs):
#         result = pages_filter(request, CustomUser, CustomUserSerializer)
#         return Response(result)    