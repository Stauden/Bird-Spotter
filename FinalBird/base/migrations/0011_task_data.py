# Generated by Django 4.2.7 on 2023-12-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_task_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='data',
            field=models.TextField(blank=True, null=True),
        ),
    ]