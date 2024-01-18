# Generated by Django 5.0 on 2024-01-01 18:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0024_alter_usernotice_response'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernotice',
            name='complaint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grievance.complaint'),
        ),
        migrations.AlterField(
            model_name='usernotice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
