# Generated by Django 3.1.3 on 2020-11-29 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('ssc_memo', models.ImageField(upload_to='images/')),
                ('inter_memo', models.ImageField(upload_to='images/')),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_father_name', models.CharField(max_length=100)),
                ('student_mother_name', models.CharField(max_length=100)),
                ('student_mobile', models.CharField(max_length=100)),
                ('student_profile_photo', models.ImageField(upload_to='images/')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.department')),
                ('student_apps', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.studentapp')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
