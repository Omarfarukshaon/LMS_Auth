from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from _applib.model_choice_fields import TeacherStatus, TeacherGender


class Teacher(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='teacher_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='teacher_set',
        blank=True
    )

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11, blank=True, unique=True)
    profile_picture = models.CharField(max_length=300)
    gender = models.CharField(max_length=10, choices=TeacherGender.CHOICES, blank=True)
    is_verified = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=TeacherStatus.CHOICES, default=TeacherStatus.PENDING)
    website = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    def __str__(self):
        return f"Full_name: {self.full_name} || Phone: {self.phone} || Status: {self.status}"

    class Meta:
        db_table = 'Teacher'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['-created_at']
