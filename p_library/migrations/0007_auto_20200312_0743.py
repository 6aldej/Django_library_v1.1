# Generated by Django 2.2.6 on 2020-03-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0006_auto_20200309_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=120),
        ),
    ]
