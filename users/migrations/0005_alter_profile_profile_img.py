# Generated by Django 5.0.4 on 2024-05-17 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_contactinfo_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='default_profile_img.png', upload_to=''),
        ),
    ]
