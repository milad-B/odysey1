# Generated by Django 4.2.3 on 2023-07-17 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_chat_userip_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 13, 36, 24, 967697, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 17, 13, 36, 24, 966697, tzinfo=datetime.timezone.utc)),
        ),
    ]
