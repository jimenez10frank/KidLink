
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="administrator_profile")
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=100, choices=[
        ("manager", "Manager"),
        ("coordinator", "Coordinator"),
        ("staff", "Staff"),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

#activites class 
class Activities(models.Model):
    activity_id = models.CharField(max_length=13, primary_key=True) #costum PK name
    activity_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.activity_id} {self.activity_name} {self.description} {self.start_date} {self.end_date} {self.location}"