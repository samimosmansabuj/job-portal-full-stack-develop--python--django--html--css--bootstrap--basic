# Generated by Django 5.0 on 2023-12-26 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=900)),
                ('job_details', models.TextField(blank=True, null=True)),
                ('vacancy', models.CharField(blank=True, default='Not specific', max_length=50, null=True)),
                ('salary', models.PositiveIntegerField(blank=True, null=True)),
                ('employment_status', models.CharField(blank=True, choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Remote', 'Remote')], max_length=50, null=True)),
                ('gender_allow', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both')], max_length=50, null=True)),
                ('application_deadline', models.DateField(blank=True, null=True)),
                ('published_date', models.DateField(auto_now_add=True)),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.recruiter_profile')),
            ],
        ),
    ]