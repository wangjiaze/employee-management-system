from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Attendance
from .serializers import AttendanceSerializer
from employees.permission import IsEmployeeUser

class AttendanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing attendance records.
    
    This endpoint allows you to:
    - List attendance records
    - Create a new attendance record
    - Retrieve a specific attendance record
    - Update an attendance record
    - Delete an attendance record
    
    Admin, HR, and employees can access this endpoint.
    Employees can only view their own attendance records.
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['employee', 'date', 'status']
    ordering_fields = ['date', 'employee']
    permission_classes = [IsEmployeeUser]  # Admin, HR, and employees can access attendance records