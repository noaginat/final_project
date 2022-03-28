from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets, permissions


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


def employees_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employees_data.html', {"employees": employees})


def employee_details(request, slug):
    employee = Employee.objects.get(slug=slug)
    return render(request, 'employees/employee_details.html', {"employee": employee})
