# Generated by Django 4.1.2 on 2022-10-16 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
        ('medias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.room'),
        ),
    ]
