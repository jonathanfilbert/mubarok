# Generated by Django 3.0.6 on 2020-05-16 10:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200516_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesan',
            name='secret',
            field=models.CharField(default=uuid.UUID('9d8f015e-4e81-4fbb-bcc6-cab0c82d1454'), editable=False, max_length=10, unique=True),
        ),
    ]
