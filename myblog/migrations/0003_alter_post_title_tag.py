# Generated by Django 4.0.1 on 2022-05-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
