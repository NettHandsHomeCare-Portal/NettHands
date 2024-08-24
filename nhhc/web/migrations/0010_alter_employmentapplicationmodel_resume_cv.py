# Generated by Django 5.0.8 on 2024-08-21 07:07

import nhhc.utils.upload
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0009_alter_employmentapplicationmodel_resume_cv"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employmentapplicationmodel",
            name="resume_cv",
            field=models.FileField(blank=True, null=True, upload_to=nhhc.utils.upload.UploadHandler.generate_randomized_file_name),
        ),
    ]
