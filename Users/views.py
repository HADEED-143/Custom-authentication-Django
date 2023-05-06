from django.shortcuts import render
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status

from . import permissions
from .serializers import UserSerializer, LaborerRegistrationSerializer, EmployerRegistrationSerializer, \
    ContractorRegistrationSerializer
from rest_framework.authtoken.models import Token


# Create your views here.
class EmployerRegistrationView(generics.GenericAPIView):
    serializer_class = EmployerRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "User Created Successfully.  Now perform Login to get your token"
        })
    def get(self, request, *args, **kwargs):
        return Response({
            "message": "This is a post request"
        })
    def put(self, request, *args, **kwargs):
        return Response({
            "message": "This is a post request"
        })
    def delete(self, request, *args, **kwargs):
        return Response({
            "message": "This is a post request"
        })

class LaborerRegistrationView(generics.GenericAPIView):
    serializer_class = LaborerRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "User Created Successfully.  Now perform Login to get your token"
        })
    def get(self, request, *args, **kwargs):
        return Response({
            "message": "This is a post request"
        })
    def put(self, request, *args, **kwargs):
        return Response({
            "message": "This is a post request"
        })
    def delete(self, request, *args, **kwargs):
        return Response({
            "message": "This is a post request"
        })


class ContractorRegistrationView(generics.GenericAPIView):
    serializer_class = ContractorRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "User Created Successfully.  Now perform Login to get your token"
        })
    def get(self, request, *args, **kwargs):
        return Response({
            "message": "This is a post request"
        })
    def put(self, request, *args, **kwargs):
        return Response({
            "message": "This is a post request"
        })
    def delete(self, request, *args, **kwargs):
        return Response({
            "message": "This is a post request"
        })


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_employer': user.is_employer,
            'is_laborer': user.is_laborer,
            'is_contractor': user.is_contractor,


        })


class LogoutView(generics.GenericAPIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class IsEmployer:
    pass


class EmployerOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response(data="Only for employees!", status=status.HTTP_200_OK)


class IsLaborer:
    pass


class LaborerOnlyView(generics.RetrieveAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response(data="Only for Laborers!", status=status.HTTP_200_OK)


class IsContractor:
    pass


class ContractorOnlyView(generics.RetrieveAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response(data="Only for Contractors!", status=status.HTTP_200_OK)