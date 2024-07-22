from rest_framework import serializers
from django.contrib.auth.models import User

from admin_custom.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = ['username', 'first_name','last_name']