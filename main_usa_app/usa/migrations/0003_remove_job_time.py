# Generated by Django 5.0 on 2023-12-13 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("usa", "0002_alter_job_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="time",
        ),
    ]