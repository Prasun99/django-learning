from django.shortcuts import render
from . forms import studentForm
def student_create(request):
  form = studentForm()

  if request.method =="POST":
    form =studentForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request,'success.html')
  return render(request,'student.html',{'form':form})