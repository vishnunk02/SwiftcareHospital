from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.

class Designation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    options2=(
        ("Default","Default"),
        ("cardiology","cardiology"),
        ("oncology","oncology"),
        ("orthopedics","orthopedics"),
        ("Gynacologist","Gynacologist"),
    )
    section=models.CharField(max_length=20,choices=options2,default="Default")
    options1=(
        ("doctor","doctor"),
        ("booking","booking"),
        ("lab","lab"),
        ("Default","Default"),
        ("admin","admin")
    )
    designation=models.CharField(max_length=20,choices=options1,default="Default")
    
    def __str__(self):
        return self.user.username
    
    
    
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=3)
    sex = models.CharField(max_length=10)
    phno = models.CharField(max_length=15)
    def __str__(self):
        return self.user.username
    
    
    
class Consult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='patient_name')
    doc = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_name')
    con_id = models.ForeignKey(Patient, on_delete=models.CASCADE , related_name='consult_name')
    options2 = (
        ("pending", "pending"),
        ("consulted", "consulted"),
        ("canceld", "canceld"),
    )
    status = models.CharField(max_length=20, choices=options2, default="pending")
    date = models.CharField(max_length=10)
    options2=(
        ("Default","Default"),
        ("cardiology","cardiology"),
        ("oncology","oncology"),
        ("orthopedics","orthopedics"),
        ("Gynacologist","Gynacologist"),
    )
    section=models.CharField(max_length=20,choices=options2,default="Default")
    symptoms = models.CharField(max_length=1000)
    tests = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.user.username
    
    
    
    
class Prescription(models.Model):
    presc_id = models.ForeignKey(Consult, on_delete=models.CASCADE , related_name='prescription_name')
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='pres_name')
    doc = models.ForeignKey(User, on_delete=models.CASCADE, related_name='presd_name')
    medicine = models.CharField(max_length=100)
    routine = models.CharField(max_length=50)
    days = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.username