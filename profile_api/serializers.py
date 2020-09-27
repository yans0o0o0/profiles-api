from rest_framework import serializers

from profile_api import models

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'lastname', 'password')
        extra_kwargs={
            'password':{
                'write_only': True,
                'style':{
                     'input_type':'password'
                }
            }
        }

    def create(request, validated_data):

        user = models.UserProfile.objects.create_user(
            email= validated_data['email'],
            name= validated_data['name'],
            lastname= validated_data['lastname'],
            password= validated_data['password'],
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
