# Generated by Django 5.0 on 2023-12-30 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0011_customuser_delete_userdata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]