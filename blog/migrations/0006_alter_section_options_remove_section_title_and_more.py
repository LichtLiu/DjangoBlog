# Generated by Django 4.2.16 on 2024-09-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_article_views"),
    ]

    operations = [
        migrations.AlterModelOptions(name="section", options={"ordering": ["order"]},),
        migrations.RemoveField(model_name="section", name="title",),
        migrations.AddField(
            model_name="section", name="order", field=models.IntegerField(default=0),
        ),
    ]
