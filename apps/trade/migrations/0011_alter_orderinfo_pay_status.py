# Generated by Django 3.2.7 on 2021-12-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0010_remove_ordergoods_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.BooleanField(default=False, max_length=100, verbose_name='订单状态'),
        ),
    ]
