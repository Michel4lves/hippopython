# Generated by Django 4.0.5 on 2022-06-10 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='vimeo_id',
            field=models.CharField(default=12345, max_length=32),
        ),
    ]