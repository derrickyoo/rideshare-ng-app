# Generated by Django 3.1.1 on 2020-09-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20200915_2042"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="photos"),
        ),
    ]
