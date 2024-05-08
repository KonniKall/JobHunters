# Generated by Django 5.0.4 on 2024-05-06 19:39

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_work_experience_workexperience'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='')),
                ('location', models.CharField(default='')),
                ('category', models.CharField(default='')),
                ('work_type', models.TextField(default='')),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='job_listing',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.joblisting'),
        ),
    ]