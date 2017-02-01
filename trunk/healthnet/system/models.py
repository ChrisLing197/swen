from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

# User model
class Registration(models.Model):
    DOCTOR = "DR"
    PATIENT = "PT"
    NURSE = "NR"
    ADMIN = "AD"

    ROLE_TYPE_CHOICES = (
            (DOCTOR, "Doctor"),
            (PATIENT, "Patient"),
            (NURSE, "Nurse"),
            (ADMIN, "Admin")
        )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    primary_care =  models.ForeignKey("self",
            related_name="primary_patients",
            limit_choices_to={'role': DOCTOR},
            blank=True, null=True
        )
    doctors = models.ManyToManyField('self',
            related_name="patients",
            limit_choices_to={'role': DOCTOR})

    role = models.CharField(
            max_length=2,
            choices=ROLE_TYPE_CHOICES,
            default=PATIENT
        )
    in_hospital      = models.BooleanField(default=False)
    date_registered = models.DateField(auto_now=True)
    date_of_birth   = models.DateField(blank=True,null=True)
    phone_number    = models.CharField(max_length=10,blank=True,null=True)
    mail_address    = models.TextField(blank=True,null=True)

    hospital        = models.ForeignKey('Hospital',
                        related_name="patients",
                        blank=True,null=True)

    employed_hospital = models.ForeignKey('Hospital',
                related_name="doctors",
                blank=True,null=True)

    def __str__(self):
        return self.user.username

# Data Models

class Hospital(models.Model):
    name    = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey("Registration",
            limit_choices_to={'role': Registration.PATIENT},
            related_name="appointments_patient"
        )
    doctor = models.ForeignKey("Registration",
            limit_choices_to={'role': Registration.DOCTOR},
            related_name="appointments_doctor"
        )

    date_created = models.DateTimeField(auto_now=True)
    date_scheduled = models.DateTimeField()

    def __str__(self):
        return "["+self.date_scheduled.isoformat()+"]"+self.doctor

class Record(models.Model):
    DIAGNOSIS = "DG"
    TEST_RESULTS = "TR"
    HOSPITAL = "HR"
    SYMPTOMS = "SY"
    PRESCRIPTION = "RX"

    RECORD_TYPE_CHOICES = (
            (DIAGNOSIS, "Diagnosis"),
            (TEST_RESULTS, "Test Results"),
            (HOSPITAL, "Hospital Record"),
            (SYMPTOMS, "Symptoms"),
            (PRESCRIPTION, "Prescription")
        )

    patient = models.ForeignKey("Registration",
            limit_choices_to={'role': Registration.PATIENT},
            related_name="records_patient"
        )
    patient_readable = models.BooleanField(default=False)
    doctor  = models.ForeignKey("Registration",
            limit_choices_to=(Q(role__exact=Registration.DOCTOR)|Q(role__exact=Registration.NURSE)),
            related_name="records_doctor"
        )

    record_type = models.CharField(
            max_length=2,
            choices=RECORD_TYPE_CHOICES
        )
    doctors_note = models.TextField()

class Activity(models.Model):
    REGISTRATION = "RG"
    APPOINTMENT = "AP"
    PRESCRIPTION = "PS"
    RECORD = "RC"
    LOGIN = "LG"

    ACTIVITY_TYPE_CHOICES = (
            (REGISTRATION,"Registration"),
            (APPOINTMENT,"Appointment"),
            (PRESCRIPTION,"Prescription"),
            (RECORD,"Record"),
            (LOGIN,"Login"),
        )
    
    activity_type = models.CharField(
                max_length=2,
                choices=ACTIVITY_TYPE_CHOICES
            )
    timestamp = models.DateTimeField(auto_now=True)
    user_responsible = models.ForeignKey("Registration")
    description = models.TextField()

    def __str__(self):
        return "["+self.timestamp.isoformat()+"] "+str(self.user_responsible)+"|"+self.activity_type+"-"+self.description

class Message(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey("Registration",
            related_name="sent_messages")
    recipient = models.ForeignKey("Registration",
            related_name="received_messages")
    text = models.TextField()

    def __str__(self):
        return "["+self.timestamp.isoformat()+"]"+str(self.sender)+"|"+str(self.recipient)
