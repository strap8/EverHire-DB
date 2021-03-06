from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    # author_name = serializers.CharField(source='author_name')
    class Meta:
        model = User
        fields = (
        'id', 'username', 'password', 'email', 'bio', 'first_name', 'last_name',
        'profile_image',)
        write_only_fields = ('password',)
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('date_joined',)


    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password = make_password(validated_data['password'])
            )
        user.set_password(validated_data["password"])
        user.save()
        return user

    # def create_user(self, username, email, password=None):
    #     if username is None:
    #         raise TypeError('Users must have a username.')

    #     if email is None:
    #         raise TypeError('Users must have an email address.')

    #     user = User(email=validated_data['email'], username=validated_data['username'])
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


    # def restore_object(self, attrs, instance=None):
    #     # call set_password on user object. Without this
    #     # the password will be stored in plain text.
    #     user = super(UserSerializer, self).restore_object(attrs, instance)
    #     user.set_password(attrs['password'])
    #     return user
