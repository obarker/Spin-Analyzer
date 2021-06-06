from rest_framework import serializers
from .models import Users


# serialize the fields from the model.

# UserSerializer is the master serializer for all the User data.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','username','subscription_level','created_at')



