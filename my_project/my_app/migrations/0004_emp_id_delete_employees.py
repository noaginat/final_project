# Generated by Django 4.0 on 2022-03-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_employee_general'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp_id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
    ]
