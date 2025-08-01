from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'status', 'is_verified', 'gender', 'created_at')
    list_filter = ('status', 'gender', 'is_verified', 'created_at')
    search_fields = ('email', 'full_name', 'phone')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'full_name', 'phone', 'profile_picture', 'gender', 'status', 'is_verified', 'website')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )
