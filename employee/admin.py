from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from employee.models import Department, Employee

admin.site.register(
    Department,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title'
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(Employee)
