from django.db import models
from employees.models import Employee

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performances')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 rating
    review_date = models.DateField()
    comments = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.employee.name} - {self.review_date} - Rating: {self.rating}"