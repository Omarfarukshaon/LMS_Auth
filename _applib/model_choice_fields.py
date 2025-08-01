# _applib/model_choice_fields.py

class TeacherStatus:
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PENDING = 'pending'

    CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (PENDING, 'Pending'),
    ]

class TeacherGender:
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
