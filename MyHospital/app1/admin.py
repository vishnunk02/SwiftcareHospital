from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Designation)
admin.site.register(Consult)
admin.site.register(Patient)
admin.site.register(Prescription)