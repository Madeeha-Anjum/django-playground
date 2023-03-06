# Generated by Django 4.1.5 on 2023-01-29 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("title", models.CharField(max_length=100)),
                ("memo", models.TextField(blank=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("completed", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]