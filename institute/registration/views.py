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
        return HttpResponseRedirect(reverse('institute:index'))
    return render(request, 'institute/application.html')


def student_registration(request):
    if request.method == "POST":
        email = request.POST['student_email']
        stu = StudentApp.objects.get(email=email, is_verified=True)
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['student_email']
        )
        dept = Department.objects.get(department_name=request.POST['department_name'])
        if stu.email == user.email:
            Student_reg.objects.create(
                student_apps=stu,
                student_name=request.POST['student_name'],
                student_email=request.POST['student_email'],
                student_father_name=request.POST['student_father_name'],
                student_mother_name=request.POST['student_mother_name'],
                student_mobile=request.POST['student_mobile'],
                student_profile_photo=request.FILES['student_profile_photo'],
                department=dept,
                user=user,
            )
        return HttpResponseRedirect(reverse('institute:index'))
    return render(request, 'institute/student_registration.html')


def student_list(request, department=None):
    st_list = Student_reg.objects.filter(department="")
    return render(request, 'institute/student_list.html', {'st_list': st_list})

