from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from .filters import EmployeeFilter
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .permission import IsAdminUser, IsHRUser

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing departments.
    
    This endpoint allows you to:
    - List all departments
    - Create a new department
    - Retrieve a specific department
    - Update a department
    - Delete a department
    
    Only admin users can access this endpoint.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminUser]  # Only admin users can manage departments
    
    @swagger_auto_schema(
        operation_description="List all departments",
        responses={200: DepartmentSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Create a new department",
        request_body=DepartmentSerializer,
        responses={201: DepartmentSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing employees.
    
    This endpoint allows you to:
    - List all employees with filtering and search
    - Create a new employee
    - Retrieve a specific employee
    - Update an employee
    - Delete an employee
    
    You can filter employees by:
    - Department
    - Name
    - Email
    - Address
    
    You can also search employees by:
    - Name
    - Email
    - Address
    
    Only HR and admin users can access this endpoint.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = EmployeeFilter
    ordering_fields = ['name', 'date_joined', 'department']
    search_fields = ['name', 'email', 'address']
    permission_classes = [IsHRUser]  # HR and admin users can manage employees
    
    @swagger_auto_schema(
        operation_description="List all employees with filtering and search",
        manual_parameters=[
            openapi.Parameter('department', openapi.IN_QUERY, description="Filter by department ID", type=openapi.TYPE_INTEGER),
            openapi.Parameter('name', openapi.IN_QUERY, description="Filter by name", type=openapi.TYPE_STRING),
            openapi.Parameter('email', openapi.IN_QUERY, description="Filter by email", type=openapi.TYPE_STRING),
            openapi.Parameter('address', openapi.IN_QUERY, description="Filter by address", type=openapi.TYPE_STRING),
            openapi.Parameter('ordering', openapi.IN_QUERY, description="Order by field (name, date_joined, department)", type=openapi.TYPE_STRING),
            openapi.Parameter('search', openapi.IN_QUERY, description="Search in name, email, address", type=openapi.TYPE_STRING),
        ],
        responses={200: EmployeeSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Create a new employee",
        request_body=EmployeeSerializer,
        responses={201: EmployeeSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)