# Generated by Django 3.2.7 on 2021-11-25 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_userprofile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, default=' ', max_length=30, verbose_name='姓名'),
        ),
    ]
