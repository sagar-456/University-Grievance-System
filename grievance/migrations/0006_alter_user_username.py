# Generated by Django 5.0 on 2023-12-30 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0005_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='default', max_length=255, primary_key=True, serialize=False),
        ),
    ]
