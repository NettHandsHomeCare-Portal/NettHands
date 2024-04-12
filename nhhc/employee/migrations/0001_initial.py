# Generated by Django 5.0.2 on 2024-04-12 15:18

import django.utils.timezone
import django_prometheus.models
import localflavor.us.models
import nhhc.backends.storage_backends
import pgcrypto.fields
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("username", models.CharField(max_length=150)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("X", "Non-Gendered"),
                            ("B", "Binary"),
                        ],
                        default="X",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ENGLISH", "English"),
                            ("CHINESE", "Ethnic Chinese"),
                            ("GREEK", "Greek"),
                            ("ITALIAN", "Italian"),
                            ("LAOTIAN", "Laotian"),
                            ("ROMANIAN", "Romanian"),
                            ("TAGALOG", "Tagalog"),
                            ("YIDDISH", "Yiddish"),
                            ("ARABIC", "Arabic"),
                            ("FARSI", "Farsi"),
                            ("GUJARATI", "Gujarati"),
                            ("JAPANESE", "Japanese"),
                            ("LITHUANIAN", "Lithuanian"),
                            ("RUSSIAN", "Russian"),
                            ("UKRANIAN", "Ukranian"),
                            ("YUGOSLAVIAN", "Yugoslavian"),
                            ("ASSYRIAN", "Assyrian"),
                            ("FRENCH", "French"),
                            ("CREOLE", "Haitian Creole"),
                            ("MON-KHMER", "Mon-Khmer"),
                            ("MANDARIN", "Mandarin"),
                            ("SPANISH", "Spanish"),
                            ("URDU", "Urdu"),
                            ("CANTONESE", "Cantonese"),
                            ("GERMAN", "German"),
                            ("HINDI", "Hindi"),
                            ("KOREAN", "Korean"),
                            ("POLISH", "Polish"),
                            ("SWEDISH", "Swedish"),
                            ("VIETNAMESE", "Vietnamese"),
                        ],
                        default="ENGLISH",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "social_security",
                    pgcrypto.fields.EncryptedTextField(
                        blank=True,
                        charset="utf-8",
                        check_armor=True,
                        cipher="aes",
                        null=True,
                        unique=True,
                        versioned=False,
                    ),
                ),
                (
                    "date_of_birth",
                    pgcrypto.fields.EncryptedDateField(
                        blank=True,
                        charset="utf-8",
                        check_armor=True,
                        cipher="aes",
                        null=True,
                        versioned=False,
                    ),
                ),
                (
                    "middle_name",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "street_address1",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "street_address2",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "marital_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("M", "Married"),
                            ("D", "Divorced"),
                            ("S", "Separated"),
                            ("W", "Widowed"),
                            ("NM", "Never Married"),
                        ],
                        default="NM",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "emergency_contact_first_name",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "emergency_contact_last_name",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "race",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("BLACK", "Black/African American"),
                            ("NATIVE", "American Indian/Alaska Native"),
                            ("ASIAN", "Asian"),
                            ("HAWAIIAN", "Native Hawaiian/Other Pacific Islander"),
                            ("WHITE", "White/Caucasian"),
                            ("OTHER", "Other Race"),
                            ("BI_RACIAL", "Two or More Races"),
                            ("UNKNOWN", "Unknown"),
                            ("REFUSED", "Perfer Not To Disclose"),
                        ],
                        default="UNKNOWN",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "emergency_contact_relationship",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "emergency_contact_phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region="US"
                    ),
                ),
                (
                    "city",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "qualifications_verification",
                    models.FileField(
                        blank=True,
                        null=True,
                        storage=nhhc.backends.storage_backends.PrivateMediaStorage(),
                        upload_to="verifications_resumes",
                    ),
                ),
                (
                    "cpr_verification",
                    models.FileField(
                        blank=True,
                        null=True,
                        storage=nhhc.backends.storage_backends.PrivateMediaStorage(),
                        upload_to="verifications_cpr",
                    ),
                ),
                (
                    "family_hca",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("true", "Yes, I am Related to my patient"),
                            ("false", "No, I am NOT Related to my patient"),
                        ],
                        default="false",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, null=True, region=None
                    ),
                ),
                ("state", localflavor.us.models.USStateField(max_length=2, null=True)),
                (
                    "ethnicity",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("NON-HISPANIC", "Non-Hispanic/Latino"),
                            ("HISPANIC", "Hispanic/Latino"),
                            ("UNKNOWN", "Unknown"),
                            ("REFUSED", "Perfer Not To Disclose"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "zipcode",
                    localflavor.us.models.USZipCodeField(max_length=10, null=True),
                ),
                ("application_id", models.BigIntegerField(default=0, unique=True)),
                ("hire_date", models.DateField(auto_now=True)),
                ("termination_date", models.DateField(blank=True, null=True)),
                (
                    "qualifications",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("HIGH_SCHOOL_GED", "High School Diploma/GED"),
                            ("CNA", "Certified Nursing Assistant (CNA)"),
                            ("LPN", "LPN"),
                            ("RN", "Registered Nurse (RN)"),
                            ("EXPERIENCE", "Applicable Experience"),
                            ("BACHELORS", "Bachelor's degree"),
                            ("MASTERS", "Master’s degree and above"),
                            ("O", "Other"),
                        ],
                        default="HIGH_SCHOOL_GED",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("in_compliance", models.BooleanField(default=False, null=True)),
                ("onboarded", models.DateField(blank=True, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Agency Employee",
                "verbose_name_plural": "Agency Employees",
                "db_table": "employee",
                "ordering": ["last_name", "first_name", "-hire_date"],
                "get_latest_by": "-date_joined",
                "unique_together": {("username", "email")},
            },
            bases=(
                models.Model,
                django_prometheus.models.ExportModelOperationsMixin("employee"),
            ),
        ),
    ]
