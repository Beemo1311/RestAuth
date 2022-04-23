from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AboutUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email'
        )


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUser
        fields = '__all__'

class AboutInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer()


    class Meta:
        model = AboutUser
        fields = '__all__'