# Generated by Django 3.2.7 on 2021-12-05 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_verifycode_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2021, 12, 5, 16, 26, 23, 24606), verbose_name='添加时间'),
        ),
    ]
