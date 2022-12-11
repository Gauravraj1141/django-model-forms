from django.shortcuts import render
from .forms import register, login, Studentform, Teacherform
# Create your views here.


def myhome(request):
    fm = register()
    mylog = login()
    return render(request, "fmapp/index.html", {"fm": fm, "log": mylog})


def home(request):
    stu = Studentform()
    tea = Teacherform()
    return render(request, "fmapp/index.html", {"student": stu, "teacher": tea})
