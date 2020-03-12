from django.conf.urls import url
from django.urls import path
from dataset.views import EmployeeData, EmployeeAdd, EmployeeUpdate, EmployeeDelete, EmployeeSearch,\
    DepartmentData, DepartmentAdd, DepartmentDelete

urlpatterns = [
    url(r'^employee$', EmployeeData.as_view()),
    url(r'^employee/(?P<id>[EI].[0-9]*)$', EmployeeData.as_view()),
    url(r'^employee/add$', EmployeeAdd.as_view()),
    url(r'^employee/update$', EmployeeUpdate.as_view()),
    url(r'^employee/delete/(?P<id>[EI].[0-9]*)$', EmployeeDelete.as_view()),
    url(r'^employee/search$', EmployeeSearch.as_view()),

    url(r'^department$', DepartmentData.as_view()),
    url(r'^department/(?P<id>[D].[0-9]*)$', DepartmentData.as_view()),
    url(r'^department/add$', DepartmentAdd.as_view()),
    url(r'^department/delete$', DepartmentDelete.as_view())
]
