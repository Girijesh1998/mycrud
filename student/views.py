from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentForm
from .models import Student

# Create your views here.

def AddSudent(request):
     if request.method == 'POST':
          fm=StudentForm(request.POST)
          if fm.is_valid():
               idn=fm.cleaned_data['id']
               fn=fm.cleaned_data['fname']
               ln=fm.cleaned_data['lname']
               ro=fm.cleaned_data['roll']
               mo=fm.cleaned_data['mobile']
               em=fm.cleaned_data['email']
               reg=Student(id=idn, fname=fn, lname=ln, roll=ro, mobile=mo, email=em)
               reg.save()
               fm=StudentForm()
     else:
      fm=StudentForm()
     stud=Student.objects.all()
     return render(request, 'student/boy.html', {'form':fm,'stu':stud})


def DeleteStudent(request , id):
     if request.method == "POST":
          pi=Student.objects.get(pk=id)
          pi.delete()
          return HttpResponseRedirect('/')

def UpdateStudent(request, id):
     if request.method == "POST":
          up = Student.objects.get(pk=id)
          fm=StudentForm(request.POST, instance=up)
          if fm.is_valid():
              fm.save()
              return HttpResponseRedirect('/')
     else:
         up=Student.objects.get(pk=id)
         fm=StudentForm(instance=up)
     return render(request, 'student/StudentUpdate.html',{'form':fm})
          
          

