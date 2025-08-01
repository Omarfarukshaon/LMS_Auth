# _applib/student_choice_fields.py

class StudentStatus:
    ENROLLED = 'enrolled'
    GRADUATED = 'graduated'
    DROPPED = 'dropped'

    CHOICES = [
        (ENROLLED, 'Enrolled'),
        (GRADUATED, 'Graduated'),
        (DROPPED, 'Dropped'),
    ]

class StudentGender:
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
