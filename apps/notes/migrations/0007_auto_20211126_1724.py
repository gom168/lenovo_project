# Generated by Django 3.2.7 on 2021-11-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20211126_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercomment',
            name='note',
        ),
        migrations.AddField(
            model_name='usercomment',
            name='note_id',
            field=models.CharField(default=' ', max_length=20, verbose_name='帖子的唯一标识符'),
        ),
    ]
