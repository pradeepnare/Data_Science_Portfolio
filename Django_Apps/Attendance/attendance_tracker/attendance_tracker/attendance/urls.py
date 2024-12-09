from django.urls import path
from .views import student_list, record_attendance

urlpatterns = [
    path('', student_list, name='student_list'),
    path('record/', record_attendance, name='record_attendance'),
]
