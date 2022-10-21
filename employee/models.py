from django.db import models
from django.utils import timezone
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Department(MPTTModel):
    name = models.CharField(max_length=150, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('department', kwargs={'pk': self.pk})

    class MPTTMeta:
        order_insertion_by = ['name']


class Employee(models.Model):
    name = models.CharField(max_length=100)
    employment_position = models.CharField(max_length=200)
    employment_start_date = models.DateField(auto_now_add=False)
    salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    department = TreeForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
