from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'job_id', 'salary',
                  'manager_id', 'department_id']

#
# class TypeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Type
#         fields = ['id', 'url', 'type']



# class KindSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Kind
#         fields = ['id', 'url', 'kind']
#
#
# class SpecifiedSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Specified
#         fields = ['id', 'url', 'name', 'kind_of_job']