# Generated by Django 4.2.16 on 2024-09-21 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_article_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="page_images/"),
        ),
    ]
