# Generated by Django 5.0 on 2023-12-19 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usa", "0016_blogs_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogs",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]