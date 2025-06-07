from django.contrib import admin
from .models import Attendance, CalendarDay


@admin.register(CalendarDay)
class CalendarDayAdmin(admin.ModelAdmin):
    list_display = ('date', 'is_workday')
    list_editable = ('is_workday',)
    ordering = ('date',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'start_time', 'end_time', 'overtime', 'status')
    list_filter = ('status', 'date')
    search_fields = ('user__username',)
    actions = ['export_excel']

    def export_excel(self, request, queryset):
        # Placeholder for Excel export logic
        pass
    export_excel.short_description = 'Export selected to Excel'
