from rest_framework import serializers
from . import models as member_models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        # exclude = ('password',)
        model = User

class CreateMemberSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('user',)
        model = member_models.Member

class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('user',)
        model = member_models.Member

class MemberDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        fields = '__all__'
        model = member_models.Member


