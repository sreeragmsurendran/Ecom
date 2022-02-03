from django.db import models

# Create your models here.
class Departments (models.Model):
    DepartmentId =models.AutoField(primary_key=True)
    DepartmentName =models.CharField(max_length=400) 
class Employees (models.Model):
    EmployeesId =models.AutoField(primary_key=True)
    EmployeeName =models.CharField(max_length=400) 