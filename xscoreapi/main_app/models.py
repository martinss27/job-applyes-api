from django.db import models
from django.utils.timezone import now
import uuid

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

class Job(models.Model):
    user = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, null=True, blank=True)
    desc = models.TextField(max_length=500)
    application_date = models.DateField(auto_now=True)
    JOB_CHOICES = [
        ("hybrid", "hybrid"),
        ("remote", "remote"),
        ("in-person", "in person"),
    ]
    job_type = models.CharField(max_length=10, choices=JOB_CHOICES)
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return  f"{self.title} - {self.company}"