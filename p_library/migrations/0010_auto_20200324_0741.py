# Generated by Django 2.2.6 on 2020-03-24 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0009_auto_20200324_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='phone_number',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='vk',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
    ]
