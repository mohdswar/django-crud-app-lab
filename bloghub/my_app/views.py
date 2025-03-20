# main_app/views.py

from django.shortcuts import render
from .models import Employee
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
        return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def employees_index(request):
    employees = Employee.objects.all()
    return render(request, 'employees/index.html', { 'employees': employees })
def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    return render(request, 'employees/detail.html', { 'employee': employee })
class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'description', 'age']

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = '/employees/'