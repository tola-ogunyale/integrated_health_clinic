# Generated by Django 5.0.7 on 2024-08-01 23:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insuranceinfo',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patients.patient'),
        ),
    ]
