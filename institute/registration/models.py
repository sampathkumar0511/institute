from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class StudentApp(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    ssc_memo = models.IntegerField()
    inter_memo = models.IntegerField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.student_name


class Studentreg(models.Model):
    student_apps = models.OneToOneField(StudentApp, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    student_father_name = models.CharField(max_length=100)
    student_mother_name = models.CharField(max_length=100)
    student_mobile = models.CharField(max_length=100)
    student_profile_photo = models.ImageField(upload_to='images/')
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name
