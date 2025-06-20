# Generated by Django 5.2.3 on 2025-06-16 10:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_studentinfo_academic_year_and_more"),
    ]

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
                ("full_name", models.CharField(max_length=100)),
                (
                    "department",
                    models.CharField(
                        choices=[
                            ("CS", "Computer Science"),
                            ("IT", "Information Technology"),
                            ("IS", "Information Systems"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "academic_year",
                    models.CharField(
                        choices=[
                            ("1", "First Year"),
                            ("2", "Second Year"),
                            ("3", "Third Year"),
                            ("4", "Fourth Year"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="StudentInfo",
        ),
    ]
