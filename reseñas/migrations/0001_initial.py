# Generated by Django 5.2.3 on 2025-06-24 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('comentario', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
