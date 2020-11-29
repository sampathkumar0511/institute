from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Department, StudentApp, Student_reg
from django.contrib.auth.models import User


def index_view(request):
    return render(request, 'institute/index.html')


def application(request):
    if request.method == 'POST':
        StudentApp.objects.create(
            student_name=request.POST['student_name'],
            email=request.POST['email'],
            ssc_memo=request.POST['ssc-memo'],
            inter_memo=request.POST['inter-memo']
        )
        return HttpResponseRedirect(reverse('registration:index'))
    return render(request, 'institute/application.html')


def student_registration(request):
    if request.method == "POST":
        email = request.POST['student-email']
        stu = StudentApp.objects.get(email=email, is_verified=True)
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['student-email'],
            password=request.POST['password'],
        )
        dept = Department.objects.get(department_name=request.POST['dept'])
        if stu.email == user.email:
            Student_reg.objects.create(
                student_apps=stu,
                student_name=request.POST['student-name'],
                student_email=request.POST['student-email'],
                student_father_name=request.POST['student-father'],
                student_mother_name=request.POST['student-mother'],
                student_mobile=request.POST['student-mobile'],
                student_profile_photo=request.FILES['student-profile'],
                department=dept,
                user=user,
            )
        return HttpResponseRedirect(reverse('college:index'))
    return render(request, 'institute/student_registration.html')



