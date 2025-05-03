from django.db.models import Count
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import render
from employees.models import Department, Employee
from attendance.models import Attendance
from datetime import datetime, timedelta

def index(request):
    """Render the charts HTML page"""
    return render(request, 'charts/index.html')

@api_view(['GET'])
@permission_classes([AllowAny])
def department_distribution(request):
    """API to get employee count by department"""
    try:
        departments = Department.objects.annotate(employee_count=Count('employees'))
        
        labels = [dept.name for dept in departments]
        data = [dept.employee_count for dept in departments]
        
        return Response({
            'labels': labels,
            'data': data
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
@permission_classes([AllowAny])
def attendance_overview(request):
    """API to get attendance overview for the last 7 days"""
    try:
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=6)
        
        # Generate date range
        date_range = []
        current_date = start_date
        while current_date <= end_date:
            date_range.append(current_date)
            current_date += timedelta(days=1)
        
        # Format dates for labels
        labels = [date.strftime('%Y-%m-%d') for date in date_range]
        
        # Get attendance counts
        present_counts = []
        late_counts = []
        absent_counts = []
        
        for date in date_range:
            present_count = Attendance.objects.filter(date=date, status='present').count()
            late_count = Attendance.objects.filter(date=date, status='late').count()
            absent_count = Attendance.objects.filter(date=date, status='absent').count()
            
            present_counts.append(present_count)
            late_counts.append(late_count)
            absent_counts.append(absent_count)
        
        return Response({
            'labels': labels,
            'present': present_counts,
            'late': late_counts,
            'absent': absent_counts
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)