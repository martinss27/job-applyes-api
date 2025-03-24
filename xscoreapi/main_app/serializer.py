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
    
    def update(self, instance, validated_data):
        jobs_data = validated_data.pop('jobs', [])

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        existing_jobs = {job.id: job for job in instance.jobs.all()}

        for job_data in jobs_data:
            job_id = job_data.get('id', None)


            if job_id and job_id in existing_jobs:
                job = existing_jobs[job_id]
                for attr, value in job_data.items():
                        setattr(job, attr, value)
                job.save()
            else:
                Job.objects.create(user=instance, **job_data)
        
        return instance