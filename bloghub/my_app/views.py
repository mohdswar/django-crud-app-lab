# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
        return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Define the Employee class
class Employee:
    def __init__(self, name, description, age):
        self.name = name
        self.description = description
        self.age = age

# Create a list of Employee instances
employees = [
    Employee('Lolo', 'Kinda rude.', 3)
]

def employees_index(request):
    return render(request, 'employees/index.html', { 'employees': employees })