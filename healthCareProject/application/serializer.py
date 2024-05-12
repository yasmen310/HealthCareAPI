from rest_framework import serializers
from .models import Departments, Clinic, Location, Doctor, Appointment, Hospital, Transform, Assistant ,Patient

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'

class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = ['related_doctor_id','assistantName','assistantIMG','email']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):
    location_details = serializers.SerializerMethodField()
    departments = serializers.SerializerMethodField()
    doctors = serializers.SerializerMethodField()
    clinics = serializers.SerializerMethodField()

    class Meta:
        model = Hospital
        fields = ['id', 'hospitalName', 'hospitalIMG','description_about_hospital', 'phone','location_details','departments','doctors','clinics', 'location','available_departments','doctorsId','clinicsId']

    def get_location_details(self, obj):
        location = obj.location
        if location:
            return {
                'street': location.street,
                'city': location.city,
                'country': location.country
            }
        else:
            return {}

    def get_departments(self, obj):
        departments = obj.available_departments.all()
        return [department.departmentName for department in departments]

    def get_doctors(self, obj):
        doctors = obj.doctorsId.all()
        return [doctor.doctorName for doctor in doctors]

    def get_clinics(self, obj):
        clinics = obj.clinicsId.all()
        return [clinic.clinicName for clinic in clinics]


class ClinicSerializer(serializers.ModelSerializer):
    specialization_name = serializers.SerializerMethodField()

    class Meta:
        model = Clinic
        fields = ['id', 'clinicName', 'specialization_name', 'specialization']
      

    def get_specialization_name(self, obj):
        return obj.specialization.departmentName


class DoctorSerializer(serializers.ModelSerializer):
    specialization_name = serializers.SerializerMethodField()
    hospital_name = serializers.SerializerMethodField()
    assistant_name = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['doctor_id', 'doctorIMG', 'email' ,'doctorName','age', 'aboutMe','specialization_name', 'hospital_name','assistant_name','specialization', 'hospital']

    def get_specialization_name(self, obj):
        return obj.specialization.departmentName

    def get_hospital_name(self, obj):
        return obj.hospital.hospitalName if obj.hospital else None

    def get_assistant_name(self, obj):
        assistant = Assistant.objects.filter(related_doctor_id=obj.doctor_id).first()
        return assistant.assistantName if assistant else None


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class TransformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transform
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    location_details = serializers.SerializerMethodField()
    prescription = serializers.ImageField(required=False, allow_null=True) 
    class Meta:
        model = Patient
        fields = ['patient_id','patientIMG','patientName', 'phone','medicalHistory','email', 'location_details','prescription','location', 'email']
        extra_kwargs = {
            'location': {'required': True}  
        }

    def get_location_details(self, obj):
        return {
            'street': obj.location.street,
            'city': obj.location.city,
            'country': obj.location.country
        }






