# Generated by Django 3.2.7 on 2021-12-05 08:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_verifycode_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]
