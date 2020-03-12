from django.shortcuts import render

import os

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from dataset.models import Employee, Department
from dataset.serializers import EmployeePostSerializer, EmployeeSerializers, DepartmentSerializer
from utils.exceptions import AppException


class EmployeeData(APIView):
    def get(self, request, id=None):
        if id is None:
            objs = Employee.objects.all().order_by('id')
            emp_data = EmployeeSerializers(objs, many=True)
        else:
            objs = Employee.objects.get(emp_id=id)
            emp_data = EmployeeSerializers(objs)
        print(emp_data.data)
        return Response(emp_data.data)


class EmployeeAdd(APIView):
    def post(self, request):
        data = request.data
        serializer = EmployeePostSerializer(data=data)
        if not serializer.is_valid():
            raise AppException(serializer.errors)

        obj = Employee()
        obj.emp_id = data['emp_id']
        obj.emp_name = data['emp_name']
        obj.emp_age = data['emp_age']
        obj.emp_salary = data['emp_salary']
        dept = Department.objects.get(dept_name=data['emp_dept'])
        obj.emp_dept = dept
        obj.save()

        emp_data = EmployeeSerializers(obj)
        return Response(emp_data.data, status=status.HTTP_201_CREATED)


class EmployeeUpdate(APIView):
    def put(self, request):
        data = request.data
        obj = Employee.objects.get(emp_id=data['emp_id'])
        obj.emp_name = data["emp_name"]
        obj.emp_age = data['emp_age']
        obj.emp_salary = data['emp_salary']
        if obj.emp_dept.dept_name != data['emp_dept']:
            dept = Department.objects.get(dept_name=data['emp_dept'])
            obj.emp_dept = dept
        obj.save()
        emp_data = EmployeeSerializers(obj)
        return Response(emp_data.data)


class EmployeeDelete(APIView):
    def delete(self, requst, id=None):
        obj = Employee.objects.get(emp_id=id)
        obj.delete()
        return Response("Done")


class EmployeeSearch(APIView):
    def post(self, request):
        data = request.data
        if data['search_by'] == "department":
            obj_dept = Employee.objects.filter(emp_dept__dept_name=data['search_key'])
            emp_data = EmployeeSerializers(obj_dept, many=True)
            return Response(emp_data.data)
        elif data['search_by'] == "salary":
            obj_dept = Employee.objects.filter(emp_salary__gte=data['low_bound']).exclude(emp_salary__gte=data['high_bound'])
            emp_data = EmployeeSerializers(obj_dept, many=True)
            return Response(emp_data.data)


class DepartmentData(APIView):
    def get(self, request, id=None):
        if id is None:
            objs = Department.objects.all().order_by('id')
            emp_data = DepartmentSerializer(objs, many=True)
        else:
            objs = Department.objects.get(dept_id=id)
            emp_data = DepartmentSerializer(objs)
        return Response(emp_data.data)


class DepartmentAdd(APIView):
    def post(self, request):
        data = request.data
        serializer = DepartmentSerializer(data=data)
        if not serializer.is_valid():
            raise AppException(serializer.errors)
        data = serializer.data
        obj = Department()
        obj.dept_id = data['dept_id']
        obj.dept_name = data['dept_name']
        obj.save()

        dept_data = DepartmentSerializer(obj)
        return Response(dept_data.data, status=status.HTTP_201_CREATED)


class DepartmentDelete(APIView):
    def delete(self, request, id=None):
        obj = Department.objects.get(dept_id=id)
        obj.delete()
        return Response("Done")