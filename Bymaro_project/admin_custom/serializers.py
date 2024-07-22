# yourapp/serializers.py
import string
import random

from django.core.mail import send_mail
from rest_framework import serializers
from django.contrib.auth.models import Group

from Bymaro_project import settings
from .models import CustomUser


class AdminUserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name' , 'group' ,'chantier')

    def create(self, validated_data):
        group = validated_data.pop('group')
        chantier_id = validated_data.pop('chantier', None)
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        # Generate email and password
        email = f"{first_name.lower()}{last_name.lower()}@gmail.com"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

        user = CustomUser.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        if group:
            user.group = group
            user.groups.add(group)
        if chantier_id:
            user.chantier = chantier_id
        user.save()

        self.send_credentials_email(user, password)
        return user

    def send_credentials_email(self, user, password):
        subject = 'Your account credentials'
        message = (
            f'Hello {user.first_name},\n\n'
            f'Your account has been created successfully.\n\n'
            f'Email: {user.email}\n'
            f'Password: {password}\n\n'
            'Please log in and change your password as soon as possible.\n\n'
            'Thank you!'
        )
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

class AdminUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'group', 'is_staff' ,'is_active' ,'chantier')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'group', 'chantier','date_joined']


