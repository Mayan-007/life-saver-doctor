from django.shortcuts import render, redirect
from life_saver_user_auth.models import User
from life_saver_doctor.models import Doctor
from life_saver_appointment.models import Appointment
from life_saver_patient.models import Patient

def check_session(request):
    if request.session.has_key('user'):
        user = User.objects.get(id=request.session['user'])
        if user.role == 'doctor':
            return True
    return False

def check_profile_completion(request):
    try:
        doctor = Doctor.objects.get(user__id=request.session['user'])
        if doctor.is_profile_complete:
            return True
        return False
    except:
        return False

def index(request):
    if check_session(request):
        if check_profile_completion(request):
            doctor = Doctor.objects.get(user__id=request.session['user'])
            if doctor.is_verified:
                return render(request, 'index_doctor.html', {'doctor': doctor})
            return redirect('waitlist_doctor')
        else:
            return redirect('profile_completion_doctor')
    return redirect('login')

def profile_completion(request):
    if check_session(request):
        if not check_profile_completion(request):
            user = User.objects.get(id=request.session['user'])
            if request.method == 'POST':
                specialization = request.POST['specialization']
                qualification = request.POST['qualification']
                fees = request.POST['fees']
                experience = request.POST['experience']
                is_profile_complete = True
                doctor = Doctor(user=user, specialization=specialization, qualification=qualification, fees=fees, experience=experience, is_profile_complete=is_profile_complete)
                doctor.save()
                return redirect('index_doctor')
            else:
                try:
                    doctor = Doctor.objects.get(user=user)
                    if doctor.is_profile_complete:
                        return redirect('index_doctor')
                except:
                    return render(request, 'profile_completion_doctor.html', {'user': user})
        else:
            return redirect('index_doctor')
    return redirect('login')

def waitlist(request):
    if check_session(request):
        if check_profile_completion(request):
            doctor = Doctor.objects.get(user__id=request.session['user'])
            if doctor.is_verified:
                return redirect('index_doctor')
            return render(request, 'waitlist_doctor.html', {'user': doctor.user})
    return redirect('login')

def remove_duplicate_patients(patients):
    patients_without_duplicates = []
    for patient in patients:
        if patient not in patients_without_duplicates:
            patients_without_duplicates.append(patient)
    return patients_without_duplicates

def patients(request):
    if check_session(request):
        if check_profile_completion(request):
            doctor = Doctor.objects.get(user__id=request.session['user'])
            if doctor.is_verified:
                appointments = Appointment.objects.filter(doctor=doctor)
                patients = []
                for appointment in appointments:
                    if appointment.status != 'rejected':
                        patients.append(appointment.patient)
                patients = remove_duplicate_patients(patients)
                return render(request, 'patients_doctor.html', {'patients': patients})
            return redirect('waitlist_doctor')
    return redirect('login')

def remove_appointments(appointments):
    appointments_without_rejections = []
    for appointment in appointments:
        if appointment.status not in ['rejected', 'completed']:
            appointments_without_rejections.append(appointment)
    return appointments_without_rejections

def get_completed_appointments(appointments):
    appointments_completed = []
    for appointment in appointments:
        if appointment.is_completed:
            appointments_completed.append(appointment)
    return appointments_completed

def appointments(request):
    if check_session(request):
        if check_profile_completion(request):
            doctor = Doctor.objects.get(user__id=request.session['user'])
            if doctor.is_verified:
                appointments = remove_appointments(Appointment.objects.filter(doctor=doctor))
                return render(request, 'appointments_doctor.html', {'appointments': appointments})
            return redirect('waitlist_doctor')
    return redirect('login')

def appointment_history(request):
    if check_session(request):
        if check_profile_completion(request):
            doctor = Doctor.objects.get(user__id=request.session['user'])
            if doctor.is_verified:
                appointments = get_completed_appointments(Appointment.objects.filter(doctor=doctor))
                return render(request, 'appointments_doctor.html', {'appointments': appointments})
            return redirect('waitlist_doctor')
    return redirect('login')

def appointment(request, appointment_id):
    if check_session(request):
        if check_profile_completion(request):
            doctor = Doctor.objects.get(user__id=request.session['user'])
            if doctor.is_verified:
                appointment = Appointment.objects.get(id=appointment_id)
                appointment.patient_name = appointment.patient.user.first_name + ' ' + appointment.patient.user.last_name
                return render(request, 'appointment_doctor.html', {'appointment': appointment})
            return redirect('waitlist_doctor')
    return redirect('login')

def accept_appointment(request, appointment_id):
    if check_session(request):
        if check_profile_completion(request):
            doctor = Doctor.objects.get(user__id=request.session['user'])
            if doctor.is_verified:
                appointment = Appointment.objects.get(id=appointment_id)
                appointment.status = 'accepted'
                appointment.save()
                return redirect('appointments_doctor')
            return redirect('waitlist_doctor')
    return redirect('login')

def reject_appointment(request, appointment_id):
    if check_session(request):
        if check_profile_completion(request):
            doctor = Doctor.objects.get(user__id=request.session['user'])
            if doctor.is_verified:
                appointment = Appointment.objects.get(id=appointment_id)
                appointment.status = 'rejected'
                appointment.save()
                return redirect('appointments_doctor')
            return redirect('waitlist_doctor')
    return redirect('login')

def complete_appointment(request, appointment_id):
    if check_session(request):
        if check_profile_completion(request):
            doctor = Doctor.objects.get(user__id=request.session['user'])
            if doctor.is_verified:
                appointment = Appointment.objects.get(id=appointment_id)
                if request.method == 'POST':
                    appointment.status = 'completed'
                    appointment.is_completed = True
                    appointment.doctor_remarks = request.POST['doctor_remarks']
                    appointment.save()
                    return redirect('appointments_doctor')
                return render(request, 'complete_appointment_doctor.html', {'appointment': appointment})
            return redirect('waitlist_doctor')
    return redirect('login')