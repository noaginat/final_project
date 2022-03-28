from django.db import models


class Employee(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    job_id = models.CharField(max_length=200, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    manager_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    thumb = models.ImageField(default='default.png', blank=True)
    general = models.TextField(null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.first_name







