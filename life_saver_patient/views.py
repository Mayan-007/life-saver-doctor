from django.shortcuts import render, redirect
from life_saver_user_auth.models import User
from life_saver_patient.models import Patient
from life_saver_doctor.models import Doctor
from life_saver_appointment.models import Appointment

def check_session(request):
    if request.session.has_key('user'):
        user = User.objects.get(id=request.session['user'])
        if user.role == 'patient':
            return True
    return False

def check_profile_completion(request):
    try:
        patient = Patient.objects.get(user__id=request.session['user'])
        if patient.is_profile_complete:
            return True
        return False
    except:
        return False

def index(request):
    if check_session(request):
        if check_profile_completion(request):
            patient = Patient.objects.get(user__id=request.session['user'])
            return render(request, 'index_patient.html', {'user': patient})
        else:
            return redirect('profile_completion_patient')
    return redirect('login')

def profile_completion(request):
    if check_session(request):
        user = User.objects.get(id=request.session['user'])
        if not check_profile_completion(request):
            if request.method == 'POST':
                blood_group = request.POST['blood_group']
                weight = request.POST['weight']
                height = request.POST['height']
                age = request.POST['age']
                is_profile_complete = True
                patient = Patient(user=user, blood_group=blood_group, weight=weight, height=height, age=age, is_profile_complete=is_profile_complete)
                patient.save()
                return redirect('index_patient')
            else: # GET
                try:
                    patient = Patient.objects.get(user=user)
                    if patient.is_profile_complete:
                        return redirect('index_patient')
                except:
                    return render(request, 'profile_completion_patient.html', {'user': user})
        else:
            return redirect('index_patient')
    return redirect('login')

def doctors(request):
    if check_session(request):
        if check_profile_completion(request):
            patient = Patient.objects.get(user__id=request.session['user'])
            doctors = Doctor.objects.filter(is_verified=True)
            return render(request, 'doctors_patient.html', {'user': patient, 'doctors': doctors})
        return redirect('profile_completion_patient')
    return redirect('login')

def appointments(request):
    if check_session(request):
        if check_profile_completion(request):
            patient = Patient.objects.get(user__id=request.session['user'])
            requestedAppointments = Appointment.objects.filter(patient=patient, is_completed=False)
            previousAppointments = Appointment.objects.filter(patient=patient, is_completed=True)
            return render(request, 'appointments_patient.html', {'user': patient, 'requestedAppointments': requestedAppointments, 'previousAppointments': previousAppointments})
        return redirect('profile_completion_patient')
    return redirect('login')

def book_appointment(request, doctor_id):
    if check_session(request):
        if check_profile_completion(request):
            patient = Patient.objects.get(user__id=request.session['user'])
            doctor = Doctor.objects.get(user__id=doctor_id)
            if request.method == 'POST':
                date = request.POST['date']
                time = request.POST['time']
                patient_remarks = request.POST['patient_remarks']
                appointment = Appointment(patient=patient, doctor=doctor, date=date, time=time, patient_remarks=patient_remarks)
                appointment.save()
                return redirect('appointments_patient')
            else:
                doctor.name = doctor.user.first_name + " " + doctor.user.last_name
                print(doctor.name)
                return render(request, 'book_appointment_patient.html', {'patient': patient, 'doctor': doctor})
        return redirect('profile_completion_patient')
    return redirect('login')

def reschedule_appointment(request, appointment_id):
    if check_session(request):
        if check_profile_completion(request):
            patient = Patient.objects.get(user__id=request.session['user'])
            appointment = Appointment.objects.get(id=appointment_id)
            if request.method == 'POST':
                date = request.POST['date']
                time = request.POST['time']
                patient_remarks = request.POST['patient_remarks']
                appointment.date = date
                appointment.time = time
                appointment.patient_remarks = patient_remarks
                appointment.status = 'pending'
                appointment.save()
                return redirect('appointments_patient')
            else:
                return render(request, 'reschedule_appointment_patient.html', {'patient': patient, 'appointment': appointment})
        return redirect('profile_completion_patient')
    return redirect('login')

def cancel_appointment(request, appointment_id):
    if check_session(request):
        if check_profile_completion(request):
            patient = Patient.objects.get(user__id=request.session['user'])
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.delete()
            return redirect('appointments_patient')
        return redirect('profile_completion_patient')
    return redirect('login')