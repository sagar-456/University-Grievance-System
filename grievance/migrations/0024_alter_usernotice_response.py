# Generated by Django 5.0 on 2024-01-01 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0023_usernotice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernotice',
            name='response',
            field=models.TextField(blank=True),
        ),
    ]
