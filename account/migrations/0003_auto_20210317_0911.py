# Generated by Django 3.1.7 on 2021-03-17 09:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210317_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='City',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='photo',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='profile',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
    ]
