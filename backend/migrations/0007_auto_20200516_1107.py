# Generated by Django 3.0.6 on 2020-05-16 11:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20200516_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesan',
            name='secret',
            field=models.CharField(default=uuid.UUID('6a974d4b-65c8-4153-b1b3-a2469e448764'), max_length=36, unique=True),
        ),
    ]
