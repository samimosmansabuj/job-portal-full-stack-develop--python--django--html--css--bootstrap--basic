# Generated by Django 5.0 on 2023-12-27 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_alter_saved_job_job_alter_saved_job_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saved_job',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saved_job_job', to='job.job'),
        ),
    ]
