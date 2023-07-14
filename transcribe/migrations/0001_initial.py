# Generated by Django 4.2.3 on 2023-07-14 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transcription",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("path", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("progress", models.IntegerField(default=0)),
                ("status", models.IntegerField(default=0)),
            ],
        ),
    ]