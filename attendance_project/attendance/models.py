from django.db import models
from django.contrib.auth.models import User


class CalendarDay(models.Model):
    date = models.DateField(unique=True)
    is_workday = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Calendar Day'
        verbose_name_plural = 'Calendar Days'

    def __str__(self):
        return f"{self.date}: {'Workday' if self.is_workday else 'Holiday'}"


class Attendance(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    overtime = models.DurationField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    comment = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.user.username} {self.date}"
