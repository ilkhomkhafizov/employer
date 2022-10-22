from django.shortcuts import render
from employee.models import Department, Employee
from django.core.paginator import Paginator


def listing(request, pk=1):
    page_number = request.GET.get("page", 1)
    departments = Department.objects.all()
    employers = Employee.objects.filter(department_id=pk)
    paginator = Paginator(employers, per_page=5)
    page_obj = paginator.get_page(page_number)
    department_detail = page_obj.object_list
    context = {"page_obj": page_obj, "departments": departments, "department_detail": department_detail}
    return render(request, "employee/employee.html", context)
