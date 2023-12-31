# Generated by Django 3.1.12 on 2022-02-11 06:01
import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0006_auto_20211227_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionToken',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
            ],
            options={'verbose_name': 'Connection token'},
        ),
        migrations.AlterModelOptions(
            name='accesskey',
            options={'verbose_name': 'Access key'},
        ),
        migrations.AlterModelOptions(
            name='ssotoken',
            options={'verbose_name': 'SSO token'},
        ),
    ]
