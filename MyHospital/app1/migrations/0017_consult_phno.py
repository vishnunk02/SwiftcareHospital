# Generated by Django 5.0.1 on 2024-01-27 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_consult_phno'),
    ]

    operations = [
        migrations.AddField(
            model_name='consult',
            name='phno',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app1.patient'),
            preserve_default=False,
        ),
    ]
