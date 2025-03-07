from rest_framework import serializers
from .models import UserAplications

class JobAplySerializer(serializers.ModelSerializer):
    model = UserApplications
    Fields = '__all__'