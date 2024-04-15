# Generated by Django 5.0.4 on 2024-04-13 19:03

import django.db.models.deletion
import filer.fields.file
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("employee", "0001_initial"),
        ("filer", "0017_image__transparent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="cpr_verification",
            field=filer.fields.file.FilerFileField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="cpr_verification",
                to="filer.file",
            ),
        ),
    ]