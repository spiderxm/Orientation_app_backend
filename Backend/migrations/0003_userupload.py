# Generated by Django 3.1.2 on 2020-10-20 16:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_placetovisit_distance'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserUpload',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=256, primary_key=True, serialize=False)),
                ('userId', models.CharField(max_length=256)),
                ('userName', models.CharField(max_length=256)),
                ('imageUrl', models.URLField()),
                ('userEmail', models.EmailField(max_length=254)),
                ('description', models.TextField(max_length=200)),
                ('timeOfUpload', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
