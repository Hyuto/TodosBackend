from rest_framework import serializers
from .models import Account


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Account.objects.create_user(validated_data['username'],
                                           email=validated_data['email'],
                                           password=validated_data['password'])
        return user