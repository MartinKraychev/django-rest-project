from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CreateUserSerializer(ModelSerializer):

    # hides the password in the db
    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    # remove the password from the response
    def to_representation(self, instance):
        result = super(CreateUserSerializer, self).to_representation(instance)
        result.pop('password')
        return result

    @staticmethod
    def validate_password(value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    class Meta:
        model = UserModel
        fields = ('id', UserModel.USERNAME_FIELD, 'password')


class LoginUserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password')
