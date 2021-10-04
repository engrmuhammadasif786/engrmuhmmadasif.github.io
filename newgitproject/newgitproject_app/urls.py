from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from newgitproject_app.views import UserAPIView


urlpatterns = [
    path('users/', UserAPIView.as_view(),name='users'),
]
