# Generated by Django 2.0.3 on 2021-09-28 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20190420_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='发布日期', verbose_name='发布日期'),
        ),
    ]
