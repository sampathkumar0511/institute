from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('application/', views.application, name='application'),
    path('student_registration/', views.student_registration, name='student_registration'),
    path('department_data/', views.department_data, name='department_data'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_data/', views.student_data, name='student_data'),
]
