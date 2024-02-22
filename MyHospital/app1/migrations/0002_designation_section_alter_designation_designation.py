# Generated by Django 5.0.1 on 2024-01-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='designation',
            name='section',
            field=models.CharField(choices=[('Default', 'Default'), ('cardiology', 'cardiology'), ('oncology', 'oncology'), ('orthopedics', 'orthopedics'), ('Gynacologist', 'Gynacologist')], default='Default', max_length=20),
        ),
        migrations.AlterField(
            model_name='designation',
            name='designation',
            field=models.CharField(choices=[('doctor', 'doctor'), ('booking', 'booking'), ('lab', 'lab')], default='booking', max_length=20),
        ),
    ]
