
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Administrator(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('coordinator', 'Coordinator'),
        ('staff', 'Staff'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # store hashed passwords
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Youth(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    registration_due = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# youth activities
class YouthActivity(models.Model):
    RESULT_CHOICES = [
        ('completed', 'Completed'),
    ('in_progress', 'In Progress'),
    ('not_started', 'Not Started'),
    ]
    youth = models.ForeignKey(Youth, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    participation_date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    result = models.CharField(max_length=255, blank=True, null=True, choices=RESULT_CHOICES)

    def __str__(self):
        return f"Activity {self.activity.id} for Youth {self.youth.id} on {self.participation_date}"