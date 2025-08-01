from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "status", "gender")
    list_filter = ("status", "gender")
    search_fields = ("first_name", "last_name", "email")
