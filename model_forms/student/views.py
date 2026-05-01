from django.shortcuts import render,get_object_or_404
from . forms import studentForm
from . models import student
def student_create(request):
  form = studentForm()

  if request.method =="POST":
    form =studentForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request,'success.html')
  return render(request,'student.html',{'form':form})
def student_list(request):
  students = student.objects.all()
  return render(request , 'list.html',{'students':students})
def student_detail(request,pk):
  sstudent=get_object_or_404(student,pk=pk)
  return render(request , 'detail.html',{'sstudent':sstudent})