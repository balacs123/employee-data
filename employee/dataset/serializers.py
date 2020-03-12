from rest_framework import serializers


class EmployeePostSerializer(serializers.Serializer):
    emp_id = serializers.CharField()
    emp_name = serializers.CharField()
    emp_age = serializers.IntegerField()
    emp_salary = serializers.IntegerField()
    emp_dept = serializers.CharField()


# class DepartmentPostSerializer(serializers.Serializer):
#     dept_id = serializers.CharField()
#     dept_name = serializers.CharField()


class DepartmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    dept_id = serializers.CharField()
    dept_name = serializers.CharField()


class EmployeeSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    emp_id = serializers.CharField()
    emp_name = serializers.CharField()
    emp_age = serializers.IntegerField()
    emp_salary = serializers.IntegerField()
    emp_dept = DepartmentSerializer()
