# Generated by Django 5.0 on 2023-12-31 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0013_userdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_content', models.TextField()),
            ],
        ),
    ]
