from django.shortcuts import render
from .models import Student

def home(request):
    data = Student.objects.all()
    return render(request, 'index.html', {'students': data})
