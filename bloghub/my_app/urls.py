from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('employees/', views.employees_index, name='employee-index'),
  path('employees/<int:employee_id>/', views.employee_detail, name='employee-detail'),
  path('employees/create/', views.EmployeeCreate.as_view(), name='employee-create'),
  path('employees/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='employee-update'),
  path('employees/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='employee-delete'),
]
