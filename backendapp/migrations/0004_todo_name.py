# Generated by Django 4.1.1 on 2022-10-20 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0003_todo_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='name',
            field=models.CharField(default='Undefined', max_length=200),
        ),
    ]