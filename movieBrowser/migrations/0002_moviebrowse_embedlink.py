# Generated by Django 5.1.1 on 2024-10-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movieBrowser", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="moviebrowse",
            name="embedLink",
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
