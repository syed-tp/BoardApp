# Generated by Django 5.1.1 on 2024-09-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_rename_topic_post_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
