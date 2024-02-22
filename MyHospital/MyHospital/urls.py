"""
URL configuration for MyHospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name="home"),
    path('login',LoginView.as_view(),name="login"),
    path('logout',LogOutView.as_view(),name="logout"),
    path('signup',SignUpView.as_view(),name="signup"),
    path('doclist',DoctorListView.as_view(),name="doclist"),
    path('patlist',PatientListView.as_view(),name="patlist"),
    path('doctor',DoctorView.as_view(),name="doctor"),
    path('exist',ExistUserView.as_view(),name="exist"),
    path('prisc/<int:id>',PrescriptionView.as_view(),name="prisc"),
    path('lab',LabView.as_view(),name="lab"),
    path('prelist',PrescriptionListView.as_view(),name="prelist"),
]
