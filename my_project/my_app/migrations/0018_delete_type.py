# Generated by Django 4.0 on 2022-03-28 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0017_type_delete_job_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Type',
        ),
    ]