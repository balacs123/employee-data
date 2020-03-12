from django.db import models


class Department(models.Model):
    dept_id = models.TextField(unique=True)
    dept_name = models.TextField(unique=True)


class Employee(models.Model):
    emp_id = models.TextField(unique=True)
    emp_name = models.TextField(blank=False)
    emp_age = models.IntegerField(blank=False)
    emp_salary = models.IntegerField(blank=False)
    emp_dept = models.ForeignKey(Department, on_delete=models.CASCADE)


