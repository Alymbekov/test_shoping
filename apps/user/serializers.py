from rest_framework import serializers
from .models import CustomUser

class RegistrationAPISerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=4, required=True, write_only=True)

    class Meta:
        model =  CustomUser
        fields = ('email', 'password', 'password_confirmation')

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError('Password and Password Confirmation do not match!')
        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

