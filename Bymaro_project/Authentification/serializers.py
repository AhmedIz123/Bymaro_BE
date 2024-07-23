from rest_framework import serializers
from django.contrib.auth.models import User

from admin_custom.models import CustomUser

'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'group', 'is_staff' ,'is_active' ,'chantier' , 'is_superuser','date_joined')
'''