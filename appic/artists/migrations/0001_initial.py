# Generated by Django 4.0.1 on 2023-03-13 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('music_genre', models.CharField(choices=[('rap', 'rap'), ('pop', 'pop'), ('rock', 'rock')], max_length=255)),
            ],
        ),
    ]
