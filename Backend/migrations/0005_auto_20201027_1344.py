# Generated by Django 3.1.2 on 2020-10-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0004_auto_20201027_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userupload',
            name='latitude',
            field=models.DecimalField(decimal_places=15, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='userupload',
            name='longitude',
            field=models.DecimalField(decimal_places=15, default=0, max_digits=20),
        ),
    ]
