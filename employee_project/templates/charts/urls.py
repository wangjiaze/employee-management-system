
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='chart_index'),
    path('department-distribution/', views.department_distribution, name='department_distribution'),
    path('attendance-overview/', views.attendance_overview, name='attendance_overview'),
]