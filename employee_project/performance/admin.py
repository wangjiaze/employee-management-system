from django.contrib import admin
from .models import Performance

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'review_date', 'rating', 'comments')
    list_filter = ('rating', 'review_date')
    search_fields = ('employee__name', 'comments')
