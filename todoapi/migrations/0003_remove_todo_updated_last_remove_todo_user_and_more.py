# Generated by Django 4.0.6 on 2022-07-25 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0002_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='updated_last',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
        migrations.AlterField(
            model_name='todo',
            name='completed_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
