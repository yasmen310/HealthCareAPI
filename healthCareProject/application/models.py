from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime, time
from django.db.models.signals import post_save
from django.dispatch import receiver

class Departments(models.Model):
    departmentName = models.CharField(max_length=50)

    def __str__(self):
        return self.departmentName 

class Location(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"

class Hospital(models.Model):
    hospitalName = models.CharField(max_length=100)
    hospitalIMG = models.ImageField(upload_to='HospitalIMG/', blank=True, null=True)       
    location = models.ForeignKey(Location, on_delete=models.CASCADE ,null=True, blank=True) 
    phone = models.CharField(max_length=20, blank=True, null=True)
    description_about_hospital = models.TextField()
    available_departments = models.ManyToManyField(Departments)
    clinicsId = models.ManyToManyField('Clinic')
    doctorsId=models.ManyToManyField('Doctor',related_name='hospitals')

    def __str__(self):
        return f"{self.hospitalName }, {self.location}"

class Clinic(models.Model):
    clinicName = models.CharField(max_length=50)
    specialization = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.clinicName}"

class Doctor(models.Model):
    doctorIMG = models.ImageField(upload_to='DoctorIMG/', blank=True, null=True)   
    doctorName = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True, default=0)
    email = models.EmailField(blank=True, null=True) 
    doctor_id = models.CharField(primary_key=True, max_length=8, validators=[
        RegexValidator(r'^\d{8}$', 'doctor_id must be exactly 8 digits')
    ])
    aboutMe = models.TextField(null=True, blank=True)
    specialization = models.ForeignKey(Departments, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True, blank=True)
    assistant_name = models.CharField(max_length=100, null=True, blank=True)
    assistant_requested = models.BooleanField(default=False)
    

    def __str__(self):
        return self.doctorName

    def add_assistant(self, assistant_name):
        self.assistant_name = assistant_name
        self.assistant_requested = False
        self.save()
        print("Assistant added successfully!")

class Assistant(models.Model):
    related_doctor_id = models.CharField(primary_key=True,max_length=8, validators=[
        RegexValidator(r'^\d{8}$', 'doctor_id must be exactly 8 digits')
    ])
    assistantName= models.CharField(max_length=100)
    assistantIMG = models.ImageField(upload_to='AssistantIMG/', blank=True, null=True)   
    email = models.EmailField(blank=True, null=True) 


    def __str__(self):
        return self.assistantName

@receiver(post_save, sender=Assistant)
def handle_new_assistant(sender, instance, created, **kwargs):
    if created:
        doctor_id = instance.related_doctor_id
        choice = input(f"Do you want to add {instance.assistantName} as your assistant? (yes/no): ")
        if choice.lower() == "yes":
            try:
                doctor = Doctor.objects.get(doctor_id=doctor_id)
                doctor.add_assistant(instance.assistantName)
            except Doctor.DoesNotExist:
                print("Doctor does not exist.")


class Patient(models.Model):
    patientName = models.CharField(max_length=100)
    patientIMG = models.ImageField(upload_to='PatientIMG/', blank=True, null=True)  
    phone = models.CharField(max_length=20, blank=True, null=True)
    patient_id = models.CharField(primary_key=True,max_length=14, validators=[
        RegexValidator(r'^\d{14}$', 'patient_id must be exactly 14 digits')
    ])
    medicalHistory = models.TextField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE) 
    prescription = models.ImageField(upload_to='prescriptions/', blank=True, null=True)   
    email = models.EmailField(blank=True, null=True) 
    def __str__(self):
        return self.patientName  


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    appointment_date = models.DateField(default=datetime.now)
    appointment_time = models.TimeField(default=time(hour=9, minute=0))
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE,null=True, blank=True)
    specialization = models.ForeignKey(Departments, on_delete=models.CASCADE,null=True, blank=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Appointment ID: {self.appointment_id}"


class Transform(models.Model):
    name = models.CharField(max_length=100,default="Your Name")
    age = models.IntegerField(default=0)
    reportIMG = models.ImageField(upload_to='reportIMG/', blank=True, null=True)  
    reportText = models.TextField()
    departments = models.ManyToManyField(Hospital)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.timestamp}"
