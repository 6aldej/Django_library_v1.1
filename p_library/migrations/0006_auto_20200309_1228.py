# Generated by Django 2.2.6 on 2020-03-09 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0005_auto_20200304_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='copy_count',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='p_library.Publisher'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='title',
            field=models.CharField(default=12, max_length=120),
            preserve_default=False,
        ),
    ]
