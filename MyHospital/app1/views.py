from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count
from .models import *
from .forms import *
import random

from django.template.loader import get_template
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
# Create your views here.

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data.get("username")
            p = form.cleaned_data.get("password")
            user = authenticate(request, username=u, password=p)
            if user:
                if user.is_superuser:
                    log = Designation.objects.get(user=user)
                    if log.designation == "admin":
                        login(request, user)
                        return redirect(reverse('admin:index'))
                    elif log.designation == "booking":
                        login(request, user)
                        return redirect("signup")
                    elif log.designation == "doctor":
                        login(request, user)
                        return redirect("doctor")
                    elif log.designation == "lab":
                        login(request, user)
                        return redirect("lab")
                else:
                    login(request, user)
                    return redirect('home')
            else:
                return redirect('login')
            
            
class HomeView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_superuser:
            user = request.user
            designation = Designation.objects.get(user=user)
            if designation.designation == "booking":
                return redirect('signup')
            elif designation.designation == "doctor":
                return render(request, "doctor.html")
            elif designation.designation == "lab":
                return render(request, "lab.html")
        else:
            return render(request,"index.html")
  
    
class LogOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('home')
    
    
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_superuser:
            doctors = User.objects.filter(designation__designation='doctor')
            user=request.user
            section = Designation.objects.all()
            designation = Designation.objects.get(user=user)
            if designation.designation == "booking":
                return render(request,'signup.html',{"doctors":doctors,"section":section})
            else:
                messages.success(request,"You are not authorised")
                return redirect("home")
        else:
            messages.success(request,"You are not authorised")
            return redirect("home")
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        namesuf = random.randint(1000, 9999)
        username = name + str(namesuf)
        user = User.objects.create_user(first_name=name, username=username, password=f"swiftcare{namesuf}")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        phno = request.POST.get("phno")
        Patient.objects.get_or_create(user=user, defaults={'age': age, 'sex': sex , 'phno' : phno})
        messages.success(request,f"Successfull\n your username is :{username}\npassword is :swiftcare{namesuf}")
        return redirect("exist")
    
    
    
class ExistUserView(View):
    def get(self,request,*args,**kwargs):
        patient = Patient.objects.all()
        doctors = User.objects.filter(designation__designation='doctor')
        section = Designation.objects.all()
        return render(request,"existuser.html",{"patient":patient,"doctors":doctors,"section":section})
    def post(self,request,*args,**kwargs):
        user = request.POST.get("user")
        patient = User.objects.get(id=user)
        con = Patient.objects.get(user=user)
        section = request.POST.get("section")
        doctor = request.POST.get("doctor")
        doc = User.objects.get(id=doctor)
        date = request.POST.get("date")
        print(patient,section,doc,date,con)
        Consult.objects.get_or_create(user=patient, section=section, doc=doc, date=date, con_id=con)
        return redirect("exist")
        
class DoctorListView(View):
    def get(self,request,*args,**kwargs):
        doctors = Designation.objects.filter(designation='doctor')
        return render(request,"doctorlist.html",{"doctors":doctors})
    
    
class PatientListView(View):
    def get(self,request,*args,**kwargs):
        patient = Patient.objects.all()
        return render(request,"patlist.html",{"patient":patient})
    
    
class DoctorView(View):
    def get(self,request,*args,**kwargs):
        user = request.user
        date = datetime.now().strftime('%Y-%m-%d')
        consults = Consult.objects.filter(doc=user.id, date=date)
        # for con in consults:
        #     print(con.con_id.user.id)
        return render(request, "doctor.html",{"consults":consults})

class PrescriptionView(View):
    def get(self,request,*args,**kwargs):
        user = request.user
        doctor = Designation.objects.get(user=user.id)
        id = kwargs.get("id")
        date = datetime.now().strftime('%Y-%m-%d')
        patient = Consult.objects.get(user=id ,date=date)
        date = datetime.now().strftime('%d-%m-%Y')
        return render(request, "prescription.html",{"doctor":doctor,"patient":patient,"date":date})
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        doc = request.user
        medicine = request.POST.getlist("medicine")
        routine = request.POST.getlist("routine")
        days = request.POST.getlist("days")
        user = User.objects.get(id=id)
        doctor = User.objects.get(id=doc.id)
        datenow = datetime.now().strftime('%Y-%m-%d')
        pre = Consult.objects.get(user=user,date=datenow)
        tests = request.POST.get("tests")
        symptoms = request.POST.get("symptoms")
        date = datetime.now().strftime('%Y-%m-%d')
        for m, r, d in zip(medicine, routine, days):
            Prescription.objects.create(user=user,doc=doctor,medicine=m,routine=r,days=d,date=date,presc_id=pre)
        consult_instance = Consult.objects.get(id=pre.id)
        consult_instance.symptoms = symptoms
        consult_instance.tests = tests
        consult_instance.save()
        return redirect("doctor")



class LabView(View):
    def get(self,request,*args,**kwargs):
        date = datetime.now().strftime('%Y-%m-%d')
        labcheck = Consult.objects.filter(date=date)
        lab = []
        for l in labcheck:
            if l.tests:
                lab.append(l)
                print(lab)
        return render(request, "lab.html",{"lab" : lab})
    
    
class PrescriptionListView(View):
    def get(self,request,*args,**kwargs):
        user = request.user
        prescription = Prescription.objects.filter(user=user).order_by('date')
        return render(request,"prelist.html",{"prescriptions":prescription})