# Generated by Django 5.2.3 on 2025-06-13 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Schedule",
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
                (
                    "stage",
                    models.IntegerField(
                        choices=[
                            (1, "First Year"),
                            (2, "Second Year"),
                            (3, "Third Year"),
                            (4, "Fourth Year"),
                        ]
                    ),
                ),
                (
                    "schedule_type",
                    models.CharField(
                        choices=[
                            ("lecture", "Lecture Schedule"),
                            ("exam", "Exam Schedule"),
                        ],
                        max_length=10,
                    ),
                ),
                ("image", models.ImageField(upload_to="schedules/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
