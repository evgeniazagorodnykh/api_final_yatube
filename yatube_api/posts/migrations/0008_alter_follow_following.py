# Generated by Django 3.2.16 on 2023-08-18 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_follow_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.CharField(max_length=200),
        ),
    ]
