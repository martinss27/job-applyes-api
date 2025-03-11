from rest_framework import serializers
from .models import User, Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id','title', 'company','desc','application_date','job_type','applied_on']

class UserSerializer(serializers.ModelSerializer):
    jobs = JobSerializer(many=True)

    class Meta:
        model = User
        fields = ['id','name', 'email', 'jobs']

    def create(self, validated_data):
        jobs_data = validated_data.pop('jobs')
        user = User.objects.create(**validated_data)

        for job_data in jobs_data:
            Job.objects.create(user=user, **job_data)

        return user