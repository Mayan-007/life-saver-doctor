from django.shortcuts import render, redirect
from life_saver_user_auth.models import User
from life_saver_doctor.models import Doctor
from life_saver_patient.models import Patient

def index(request):
    if request.session.has_key('user'):
        user = User.objects.get(id=request.session['user'])
        return render(request, 'index_admin.html', {'user': user})
    return redirect('login')

def doctors(request):
    if request.session.has_key('user'):
        user = User.objects.get(id=request.session['user'])
        doctors = Doctor.objects.filter(is_verified=True)
        return render(request, 'doctors_admin.html', {'user': user, 'doctors': doctors})
    
def patients(request):
    if request.session.has_key('user'):
        user = User.objects.get(id=request.session['user'])
        patients = Patient.objects.all()
        return render(request, 'patients_admin.html', {'user': user, 'patients': patients})

def waitlist(request):
    if request.session.has_key('user'):
        user = User.objects.get(id=request.session['user'])
        doctors = Doctor.objects.filter(is_verified=False)
        return render(request, 'waitlist_admin.html', {'user': user, 'doctors': doctors})
    return redirect('login')

def accept_doctor(request, doctor_id):
    if request.session.has_key('user'):
        doctor = Doctor.objects.get(user__id=doctor_id)
        doctor.is_verified = True
        doctor.save()
        return redirect('waitlist_admin')
    return redirect('login')

def reject_doctor(request, doctor_id):
    if request.session.has_key('user'):
        user = User.objects.get(id=request.session['user'])
        user.delete()
        return redirect('waitlist_admin')
    return redirect('login')

def reject_patient(request, patient_id):
    if request.session.has_key('user'):
        user = User.objects.get(id=request.session['user'])
        user.delete()
        return redirect('waitlist_admin')
    return redirect('login')