from django.db import models
from _applib.student_choice_fields import StudentStatus, StudentGender

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    status = models.CharField(
        max_length=10,
        choices=StudentStatus.CHOICES,
        default=StudentStatus.ENROLLED
    )
    gender = models.CharField(
        max_length=10,
        choices=StudentGender.CHOICES,
        default=StudentGender.OTHER
    )
    date_of_birth = models.DateField(null=True, blank=True)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
