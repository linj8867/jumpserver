# Generated by Django 2.2.10 on 2020-03-03 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0022_session_is_success'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='risk_level',
            field=models.SmallIntegerField(choices=[(0, 'Accept'), (4, 'Warning'), (5, 'Reject'), (6, 'Review & Reject'), (7, 'Review & Accept'), (8, 'Review & Cancel')], db_index=True, default=0, verbose_name='Risk level'),
        ),
    ]
