Employee Management System
A comprehensive Django-based employee management system with functionality for managing employees, tracking attendance, and performance evaluations.
Overview
This project is a web-based employee management system built with Django 5.2 and Django REST Framework. It provides functionality for:

Employee data management with department organization
Role-based access control (Admin, HR, Employee)
Attendance tracking
Performance evaluations
Data visualization and charts

Features

RESTful API for all functionality
JWT and Token-based authentication
Role-based permissions (Admin, HR, Employee)
Advanced filtering and search capabilities
Pagination for API responses
Data visualization dashboards
CRUD operations for employee and department records
User profile management with role assignments

Tech Stack

Backend: Django 5.2
API: Django REST Framework
Authentication:

JWT (JSON Web Tokens) via rest_framework_simplejwt
Token Authentication via rest_framework.authtoken
Session Authentication


Database: SQLite (default), PostgreSQL (configurable)
API Documentation: drf-yasg (Swagger/ReDoc)
Filtering & Search:

django-filter
DRF's OrderingFilter and SearchFilter


Data Visualization: Charts app and Chart.js
Development Tools:

Faker library for generating sample data



Project Structure
The project is organized into several Django apps:
1. Employees App

Manages employee data, departments, and user profiles
Implements role-based access control
Handles authentication and permissions

2. Attendance App

Tracks daily attendance records for employees
Supports multiple status types (present, absent, late)
Enforces unique constraint for employee-date combinations
Accessible to employees (own records), HR, and Admin users

3. Performance App

Tracks employee performance reviews
Supports 1-5 star rating system
Stores review dates and feedback comments
Restricted to HR and Admin users

4. Charts App

Provides data visualization for management dashboards
Includes employee distribution by department
Shows attendance overview for the past 7 days
Web interface for viewing charts

Database Structure
The system's database includes the following main models:
1. User Profile

Extension of Django's built-in User model
Roles: Admin, HR, Employee
Role-based permissions

2. Department

Department name
One-to-many relationship with employees

3. Employee

Personal information (name, email, phone, address)
Department association
Date joined
Related to attendance and performance records

4. Attendance

Employee reference (ForeignKey to Employee)
Date field for attendance record
Status field with choices (present, absent, late)
Unique constraint for employee and date combination

5. Performance

Employee reference (ForeignKey to Employee)
Rating system (1-5 scale)
Review date
Comments/feedback (optional text field)

Data Visualization
The system includes a dashboard with data visualizations powered by the Charts app:
Available Charts
1. Department Distribution Chart

Displays the number of employees in each department as a pie chart
Helps management understand workforce distribution

2. Attendance Overview Chart

Shows attendance statistics for the past 7 days as a bar chart
Tracks present, late, and absent counts for each day
Helps identify attendance patterns and trends

Dashboard Implementation

The main dashboard is rendered by the index view in the Charts app
Chart data is loaded via AJAX calls to the chart API endpoints
Visualizations are implemented using Chart.js library
Layout uses flexbox for responsive design with side-by-side charts on larger screens

Installation
Prerequisites

Python 3.x
pip
Virtual environment (recommended)
Faker library (for sample data generation)

Setup

Clone the repository
git clone https://github.com/wangjiaze/employee-management-system.git
cd employee-management-system

Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  
# On Windows: venv\Scripts\activate

Install dependencies （Django and required packages）
pip install django djangorestframework drf-yasg django-environ Faker django-filter psycopg2-binary

Configure environment variables

Create a .env file based on .env.example
Set appropriate values for database configuration and other settings


Run migrations
python manage.py migrate

Create a superuser
python manage.py createsuperuser

Generate sample data
python manage.py seed_data

Run the development server
python manage.py runserver


Database Configuration
By default, the project uses SQLite. To use PostgreSQL:

Ensure PostgreSQL is installed and running
Update the .env file with your PostgreSQL credentials:
DB_NAME=employee_db
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

Update settings.py to use the PostgreSQL configuration

Sample Data
The project includes a data seeding command to populate the database with realistic test data:
python manage.py seed_data
This command will:

Create 8 default departments (Engineering, Marketing, Finance, Human Resources, Sales, Operations, Research, Customer Support)
Generate 50 random employees with realistic names, emails, and contact information
Create attendance records for each employee for the past 30 days (excluding weekends)

70% present, 20% late, 10% absent


Generate 1-3 performance reviews per employee with random ratings and feedback

Getting Started
After installation, these steps will help you get familiar with the system:

Access the Admin Panel:

Go to http://localhost:8000/admin/
Login with your superuser credentials
Explore the admin interfaces for Employees, Departments, Attendance, and Performance


Explore the API Documentation:

Swagger UI: http://localhost:8000/swagger/
ReDoc: http://localhost:8000/redoc/


Test Authentication:

Get a JWT token: POST /api/token/
Use the token in the Authorization header: Bearer <token>
Or get a DRF token: POST /api-token-auth/


View the Dashboard:

Go to the root URL: http://localhost:8000/
Explore the department distribution and attendance charts



Development
Adding New Apps
To add a new app to the project:

Create the app:
bashpython manage.py startapp app_name

Add the app to INSTALLED_APPS in settings.py
Create models, views, serializers, and URLs
Include the app's URLs in the main urls.py
Apply migrations:
bashpython manage.py makemigrations
python manage.py migrate


Database Migrations
The project follows Django's migration system:

After making changes to models, create migration files:
bashpython manage.py makemigrations

Apply pending migrations:
bashpython manage.py migrate

View migration status:
bashpython manage.py showmigrations


 