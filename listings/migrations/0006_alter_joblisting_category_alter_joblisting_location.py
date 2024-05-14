# Generated by Django 5.0.4 on 2024-05-14 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_application_recommendations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='category',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')]),
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='location',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')]),
        ),
    ]
