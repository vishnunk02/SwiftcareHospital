# Generated by Django 5.0.1 on 2024-01-28 04:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_rename_user_id_consult_user_prescription'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='consult',
            name='con_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='consult_name', to='app1.patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescription',
            name='presc_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='prescription_name', to='app1.consult'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consult',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_name', to=settings.AUTH_USER_MODEL),
        ),
    ]