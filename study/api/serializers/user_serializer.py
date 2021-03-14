from django.contrib.auth.models import User
from rest_framework import serializers

from study.api.tasks import create_user_membership


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        create_user_membership.delay(user_id=user.id)
        return user
