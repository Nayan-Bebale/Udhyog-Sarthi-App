# Generated by Django 5.0 on 2024-01-24 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("usa", "0002_remove_job_company_job_company_description_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Company",
        ),
    ]
