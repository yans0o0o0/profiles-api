from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profile_api import serializers
from profile_api import permissions
from profile_api import models
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes= (TokenAuthentication,)
    permission_classes= (permissions.UpdateOwnProfile,)
