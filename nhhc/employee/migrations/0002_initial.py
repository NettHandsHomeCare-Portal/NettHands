# Generated by Django 5.0.4 on 2024-04-24 05:20

import django.db.models.deletion
import filer.fields.file
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("employee", "0001_initial"),
        ("filer", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="cpr_verification",
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="cpr_verification", to="filer.file"),
        ),
        migrations.AddField(
            model_name="employee",
            name="dhs_i9",
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="i9", to="filer.file"),
        ),
        migrations.AddField(
            model_name="employee",
            name="do_not_drive_agreement_attestation",
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="do_not_drive_agreement", to="filer.file"),
        ),
        migrations.AddField(
            model_name="employee",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="employee",
            name="hca_policy_attestation",
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="hca_policy", to="filer.file"),
        ),
        migrations.AddField(
            model_name="employee",
            name="idoa_agency_policies_attestation",
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="idoa_agency_policies", to="filer.file"),
        ),
        migrations.AddField(
            model_name="employee",
            name="idph_background_check_authorization",
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="idph_bg_check_auth", to="filer.file"),
        ),
        migrations.AddField(
            model_name="employee",
            name="irs_w4_attestation",
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="irs_w4", to="filer.file"),
        ),
        migrations.AddField(
            model_name="employee",
            name="job_duties_attestation",
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="job_duties", to="filer.file"),
        ),
        migrations.AddField(
            model_name="employee",
            name="marketing_recruiting_limitations_attestation",
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="marketing_recruiting_limitations", to="filer.file"),
        ),
        migrations.AddField(
            model_name="employee",
            name="qualifications_verification",
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="resume", to="filer.file"),
        ),
        migrations.AddField(
            model_name="employee",
            name="state_w4_attestation",
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="state_w4", to="filer.file"),
        ),
        migrations.AddField(
            model_name="employee",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True, help_text="Specific permissions for this user.", related_name="user_set", related_query_name="user", to="auth.permission", verbose_name="user permissions"
            ),
        ),
    ]