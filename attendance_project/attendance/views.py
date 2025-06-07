from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Attendance, CalendarDay
from django.contrib.auth.models import User


@login_required
def attendance_form(request):
    user = request.user
    days = CalendarDay.objects.order_by('date')
    if request.method == 'POST':
        for day in days:
            start = request.POST.get(f'start_{day.date}', '')
            end = request.POST.get(f'end_{day.date}', '')
            overtime = request.POST.get(f'overtime_{day.date}', '0')
            Attendance.objects.update_or_create(
                user=user,
                date=day.date,
                defaults={
                    'start_time': start or None,
                    'end_time': end or None,
                    'overtime': overtime or 0,
                }
            )
        messages.success(request, 'Attendance submitted.')
        return redirect('attendance_form')

    attendances = Attendance.objects.filter(user=user)
    context = {
        'days': days,
        'attendances': {a.date: a for a in attendances}
    }
    return render(request, 'attendance/attendance_table.html', context)


@permission_required('attendance.change_attendance')
def manage_attendance(request):
    records = Attendance.objects.select_related('user').order_by('date')
    context = {'records': records}
    return render(request, 'attendance/manage_attendance.html', context)
