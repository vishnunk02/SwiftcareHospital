# Generated by Django 5.0.1 on 2024-01-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_remove_patient_date_remove_patient_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phno',
            field=models.CharField(max_length=15),
        ),
    ]
