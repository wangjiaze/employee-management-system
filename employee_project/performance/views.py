from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Performance
from .serializers import PerformanceSerializer
from employees.permission import IsHRUser

class PerformanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing performance reviews.
    
    This endpoint allows you to:
    - List all performance reviews
    - Create a new performance review
    - Retrieve a specific performance review
    - Update a performance review
    - Delete a performance review
    
    Only HR and admin users can access this endpoint.
    """
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['employee', 'rating', 'review_date']
    ordering_fields = ['review_date', 'rating']
    permission_classes = [IsHRUser]  # HR and admin users can manage performance reviews