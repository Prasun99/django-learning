from django.shortcuts import render,get_object_or_404,redirect
from . forms import studentForm
from . models import Student
def student_create(request):
  form = studentForm()

  if request.method =="POST":
    form =studentForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request,'success.html')
  return render(request,'student.html',{'form':form})
def student_list(request):
  students = Student.objects.all()
  return render(request , 'list.html',{'students':students})
def student_detail(request,pk):
  student=get_object_or_404(Student,pk=pk)
  return render(request , 'detail.html',{'student':student})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import studentForm

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = studentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = studentForm(instance=student)

    return render(request, 'student.html', {'form': form})