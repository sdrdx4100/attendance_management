from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_form, name='attendance_form'),
    path('manage/', views.manage_attendance, name='manage_attendance'),
]
