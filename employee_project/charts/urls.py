from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='chart_index'),
    path('api/charts/department-distribution/', views.department_distribution, name='department_distribution'),
    path('api/charts/attendance-overview/', views.attendance_overview, name='attendance_overview'),
]