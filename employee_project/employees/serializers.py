from rest_framework import serializers
from .models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.ReadOnlyField(source='department.name')
    
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phone_number', 'address', 
                  'date_joined', 'department', 'department_name']