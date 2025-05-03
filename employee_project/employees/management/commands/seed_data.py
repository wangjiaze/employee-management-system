import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Department, Employee
from attendance.models import Attendance
from performance.models import Performance

class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Create departments
        departments = [
            'Engineering', 'Marketing', 'Finance', 'Human Resources', 
            'Sales', 'Operations', 'Research', 'Customer Support'
        ]
        
        dept_objects = []
        for dept in departments:
            d, created = Department.objects.get_or_create(name=dept)
            dept_objects.append(d)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created department: {dept}'))
        
        # Create employees
        employee_count = 50
        self.stdout.write(f'Creating {employee_count} employees...')
        
        for _ in range(employee_count):
            # Calculate a random join date between 1-5 years ago
            join_date = datetime.now().date() - timedelta(days=random.randint(30, 365 * 5))
            
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_joined=join_date,
                department=random.choice(dept_objects)
            )
            
            # Create attendance records for the past 30 days
            for i in range(30):
                # Skip weekends
                record_date = datetime.now().date() - timedelta(days=i)
                if record_date.weekday() >= 5:  # 5=Saturday, 6=Sunday
                    continue
                    
                # 70% present, 20% late, 10% absent
                status_choice = random.choices(
                    ['present', 'late', 'absent'], 
                    weights=[0.7, 0.2, 0.1], 
                    k=1
                )[0]
                
                Attendance.objects.create(
                    employee=employee,
                    date=record_date,
                    status=status_choice
                )
            
            # Create 1-3 performance reviews
            for _ in range(random.randint(1, 3)):
                review_date = datetime.now().date() - timedelta(days=random.randint(1, 365))
                
                Performance.objects.create(
                    employee=employee,
                    rating=random.randint(1, 5),
                    review_date=review_date,
                    comments=fake.paragraph()
                )
                
        self.stdout.write(self.style.SUCCESS(f'Successfully created {employee_count} employees with attendance and performance data'))