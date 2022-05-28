from django.db import models

# Create your models here.

class Master(models.Model):
    Email = models.EmailField(max_length=25)
    Password = models.CharField(max_length=12)
    IsActive = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'master'

Gender_choices = (
    ('m', 'male'),
    ('f', 'female')
)
class Profile(models.Model):
    ProfileImage = models.FileField(upload_to="images/users", default="user.png")
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=25, default="")
    DOB = models.DateField(auto_created=True, default="2020-01-01")
    Gender = models.CharField(max_length=10, choices=Gender_choices)
    City = models.CharField(max_length=25, default="")
    State = models.CharField(max_length=25, default="")
    Pincode = models.CharField(max_length=6, default="")
    Address = models.TextField(max_length=250, default="")
    
    
    class meta:
        db_table = 'profile'
        
Service_choices = (
    ('DC', 'Dental Checkup'),
    ('FC', 'FullBody Checkup'),
    ('ENT', 'ENT Checkup'),
    ('HC', 'Heart Checkup')
)
class Appointment(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=20, default="")
    Email = models.EmailField(max_length=25, default="")
    Book_Date = models.DateField(auto_created=True, default="2000-01-01")
    Gender = models.CharField(max_length=20, choices=Gender_choices)
    Service = models.CharField(max_length=20, choices=Service_choices)    

    class meta:
        db_table = 'appointment'