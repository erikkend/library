import django.contrib.auth
from django.contrib.auth.models import Group
from django.views.generic import CreateView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins
from rest_framework import generics
from rest_api.serializers import UserSerializer, GroupSerializer
from django.contrib.auth import get_user_model

from rest_api.permissions import IsOwnerOrReadOnly

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

