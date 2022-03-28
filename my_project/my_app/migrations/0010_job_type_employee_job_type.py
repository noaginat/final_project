# Generated by Django 4.0 on 2022-03-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_delete_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='job_type',
            field=models.ManyToManyField(to='my_app.Job_Type'),
        ),
    ]
