# Generated by Django 3.2.7 on 2021-11-25 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0002_auto_20211125_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userleavingmessage',
            name='file',
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='goods_sn',
            field=models.CharField(max_length=50, verbose_name='商品唯一货号'),
        ),
    ]
