# Generated by Django 3.2.16 on 2023-08-17 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230816_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.CharField(max_length=200),
        ),
    ]
