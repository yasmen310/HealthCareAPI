"""
URL configuration for healthCareProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from application import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'application'  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/departments/',views.DepartmentsListView.as_view(), name='api-DepartmentsListView'),
    path('api/departments/<int:pk>/',views.DepartmentsDetailView.as_view(), name='api-DepartmentsDetailView'),
]
urlpatterns += [
    path('api/clinic/',views.ClinicListView.as_view(), name='api-ClinicListView'),
    path('api/clinic/<int:pk>/',views.ClinicDetailView.as_view(), name='api-ClinicDetailView'),
]
urlpatterns += [
    path('api/location/',views.LocationListView.as_view(), name='api-LocationListView'),
    path('api/location/<int:pk>/',views.LocationDetailView.as_view(), name='api-LocationDetailView'),
]
urlpatterns += [
    path('api/doctor/',views.DoctorListView.as_view(), name='api-DoctorListView'),
    path('api/doctor/<int:pk>/',views.DoctorDetailView.as_view(), name='api-DoctorDetailView'),
]
urlpatterns += [
    path('api/hospital/',views.HospitalListView.as_view(), name='api-HospitalListView'),
    path('api/hospital/<int:pk>/',views.HospitalDetailView.as_view(), name='api-HospitalDetailView'),
]
urlpatterns += [
    path('api/appointment/',views.AppointmentListView.as_view(), name='api-AppointmentListView'),
    path('api/appointment/<int:pk>/',views.AppointmentDetailView.as_view(), name='api-AppointmentDetailView'),
]
urlpatterns += [
    path('api/transform/', views.TransformListView.as_view(), name='api-Transform-list-create'),
    path('api/transform/<int:pk>/',views.TransformDetailView.as_view(), name='api-TransformDetailView'),

]
urlpatterns += [
    path('api/assistant/', views.AssistantListView.as_view(), name='api-assistant-list-create'),
    path('api/assistant/<int:pk>/',views.AssistantDetailView.as_view(), name='api-assistantDetailView'),

]
urlpatterns += [
    path('api/patient/',views.PatientListView.as_view(), name='api-PatientListView'),
    path('api/patient/<int:pk>/',views.PatientDetailView.as_view(), name='api-PatientDetailView'),
]

