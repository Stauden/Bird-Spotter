# Generated by Django 4.2.7 on 2023-12-16 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_task_wing'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='species',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='wing',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
