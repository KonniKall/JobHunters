# Generated by Django 5.0.4 on 2024-05-17 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0014_alter_joblisting_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='job_listing',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='listings.joblisting'),
        ),
    ]