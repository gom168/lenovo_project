# Generated by Django 3.2.7 on 2021-12-05 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0006_auto_20211126_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='is_choosen',
            field=models.BooleanField(default=True, verbose_name='是否购买'),
        ),
    ]