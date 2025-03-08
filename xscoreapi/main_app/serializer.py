from rest_framework import serializers
from .models import UserApplications

class UserApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApplications
        fields = '__all__'