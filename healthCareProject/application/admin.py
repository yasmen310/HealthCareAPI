from django.contrib import admin
from .models import Departments, Clinic, Location, Doctor, Appointment, Hospital,Transform, Assistant, Patient

admin.site.register(Departments)
admin.site.register(Clinic)
admin.site.register(Location)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Hospital)
admin.site.register(Assistant)
admin.site.register(Transform)
admin.site.register(Patient)
