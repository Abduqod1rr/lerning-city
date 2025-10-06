from rest_framework import serializers
from .models import CustomUser

class UserSerializers(serializers.Serializer):
    class Meta:
        model=CustomUser
        fields=['id','username','password']
        extra_kwargs = {
            'password': {'write_only': True} # Ensure password is not shown in response
        }
        def create(self,valited_data):
         user = CustomUser.objects.create_user(**valited_data)
         return user