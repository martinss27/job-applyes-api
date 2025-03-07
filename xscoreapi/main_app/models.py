from django.db import models

# Create your models here.

class UserAplications(models.Model):
    tittle = models.CharField(max_length='300')
    company_name = models.CharField(max_length='300')
    description = models.TextField(max_length='500')
    application_date = models.DateField(auto_now=True)

    JOB_TYPE_CHOICES = [( 
    ('hybrid', 'hybrid'),
    ('remote', 'remote'),
    ('on_site', 'on_site'),)] 
    
    '''the first values are how they should appear in the database, the second ones are how they should 
    appear to users, which is why there are 2 items in each tuple'''

    job_type = models.CharField(max_length='10', choices=JOB_TYPE_CHOICES)
