# Generated by Django 4.2.3 on 2023-07-16 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='direction',
            field=models.CharField(default='user', max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 16, 19, 58, 5, 22143, tzinfo=datetime.timezone.utc)),
        ),
    ]