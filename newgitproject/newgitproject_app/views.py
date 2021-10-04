from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.utils import serializer_helpers
from rest_framework import generics, serializers, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from newgitproject_app.serializers import UserSerailizer


class UserAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerailizer
    permission_classes = [AllowAny,]