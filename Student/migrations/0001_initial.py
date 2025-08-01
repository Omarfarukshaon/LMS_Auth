# Generated by Django 5.2.4 on 2025-08-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("enrolled", "Enrolled"),
                            ("graduated", "Graduated"),
                            ("dropped", "Dropped"),
                        ],
                        default="enrolled",
                        max_length=10,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other"),
                        ],
                        default="other",
                        max_length=10,
                    ),
                ),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                ("enrollment_date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
