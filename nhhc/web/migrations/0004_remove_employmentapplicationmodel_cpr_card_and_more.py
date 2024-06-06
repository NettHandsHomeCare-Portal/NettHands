# Generated by Django 5.0.6 on 2024-06-05 04:05

import nhhc.utils.upload
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0003_alter_employmentapplicationmodel_cpr_card_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employmentapplicationmodel",
            name="cpr_card",
        ),
        migrations.AlterField(
            model_name="employmentapplicationmodel",
            name="resume_cv",
            field=models.FileField(blank=True, null=True, upload_to=nhhc.utils.upload.UploadHandler.generate_randomized_file_name),
        ),
    ]
