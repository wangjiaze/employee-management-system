import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    date_joined_after = django_filters.DateFilter(field_name='date_joined', lookup_expr='gte')
    date_joined_before = django_filters.DateFilter(field_name='date_joined', lookup_expr='lte')
    
    class Meta:
        model = Employee
        fields = ['name', 'email', 'department', 'date_joined_after', 'date_joined_before']