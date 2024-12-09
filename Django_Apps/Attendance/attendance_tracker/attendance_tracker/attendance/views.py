# Create your views here.
from django.shortcuts import render, redirect
from .models import Student, Attendance
from .forms import AttendanceForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'attendance/student_list.html', {'students': students})

def record_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/record_attendance.html', {'form': form})
