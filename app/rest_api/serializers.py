from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    custom_username = serializers.CharField(source='username', read_only=True)
    custom_email = serializers.CharField(source='email', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'custom_username', 'custom_email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
