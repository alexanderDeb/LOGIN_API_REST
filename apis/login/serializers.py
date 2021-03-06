from rest_framework import serializers
from apis.login.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import Group


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','password','username','email','name','last_name','groups','is_superuser']
        
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name','permissions']

