# Generated by Django 4.0.6 on 2022-08-22 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='recursos')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mis_recursos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
