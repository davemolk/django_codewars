# Generated by Django 3.2.9 on 2021-11-03 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katas', '0002_alter_exercise_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='languages',
            field=models.TextField(verbose_name='Langauges Used'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='tags',
            field=models.TextField(verbose_name='Kata Tags'),
        ),
    ]
