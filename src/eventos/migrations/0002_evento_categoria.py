# Generated by Django 4.0.6 on 2022-08-05 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='categoria',
            field=models.CharField(max_length=255, null=True),
            
        ),
    ]