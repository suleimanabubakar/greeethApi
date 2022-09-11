from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView,CreateAPIView,ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from accounts.serializers import ProfileSerializer
from .models import *
# Create your views here.


class MyProfile(APIView):
    def get(self,request):
        profile, created = Profile.objects.get_or_create(request.user)
        return Response(ProfileSerializer(profile).data)

    def put(self,request):
        profile, created = Profile.objects.get_or_create(request.user)
        serializer = ProfileSerializer(profile,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)