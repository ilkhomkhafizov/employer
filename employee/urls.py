from django.urls import path
from employee.views import listing

urlpatterns = [
    path('', listing, name='department'),
    path('<int:pk>/', listing, name='department_detail'),
]
