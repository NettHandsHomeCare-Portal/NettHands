# Generated by Django 5.0.4 on 2024-04-14 22:51

import django.db.models.deletion
import filer.fields.file
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("employee", "0002_alter_employee_cpr_verification"),
        ("filer", "0017_image__transparent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="qualifications_verification",
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="resume", to="filer.file"),
        ),
    ]
