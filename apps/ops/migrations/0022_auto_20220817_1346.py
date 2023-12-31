# Generated by Django 3.2.14 on 2022-08-17 05:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ops', '0021_auto_20211130_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adhocexecution',
            name='adhoc',
        ),
        migrations.RemoveField(
            model_name='adhocexecution',
            name='task',
        ),
        migrations.RemoveField(
            model_name='commandexecution',
            name='hosts',
        ),
        migrations.RemoveField(
            model_name='commandexecution',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='task',
            name='latest_adhoc',
        ),
        migrations.RemoveField(
            model_name='task',
            name='latest_execution',
        ),
        migrations.DeleteModel(
            name='AdHoc',
        ),
        migrations.DeleteModel(
            name='AdHocExecution',
        ),
        migrations.DeleteModel(
            name='CommandExecution',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel('CeleryTask'),
    ]
