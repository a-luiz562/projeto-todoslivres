# Generated by Django 3.0.2 on 2020-01-10 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dono', '0001_initial'),
        ('gatinho', '0003_gatinho_dono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gatinho',
            name='dono',
        ),
        migrations.AddField(
            model_name='gatinho',
            name='dono',
            field=models.ManyToManyField(null=True, to='dono.Dono'),
        ),
    ]
