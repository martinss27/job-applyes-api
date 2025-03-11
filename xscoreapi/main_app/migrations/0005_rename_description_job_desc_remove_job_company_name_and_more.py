# Generated by Django 5.1.6 on 2025-03-10 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_job_user_delete_userapplications_job_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='description',
            new_name='desc',
        ),
        migrations.RemoveField(
            model_name='job',
            name='company_name',
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('hybrid', 'hybrid'), ('remote', 'remote'), ('in-person', 'in person')], max_length=10),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
