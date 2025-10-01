
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
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    registration_due = models.DateField()

    def __str__(self):
        # Use first_name + last_name instead of self.user
        return f"{self.first_name} {self.last_name}"

#activities class
class Activity(models.Model):
    activity_name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        # Use activity_name instead of activity_id
        return self.activity_name

# youth activities
class YouthActivity(models.Model):
    youth = models.ForeignKey(Youth, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    participation_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)
    result = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.youth} → {self.activity}"
    
#insitute class
class Institute(models.Model):
    institute_name = models.CharField(max_length=500)
    type = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    contact_person = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()