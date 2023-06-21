from django.shortcuts import render, redirect
from life_saver_user_auth.models import User
from life_saver_doctor.models import Doctor

def index(request):
    if request.session.has_key('user'):
        user = User.objects.get(id=request.session['user'])
        if user.role == 'doctor':
            try:
                doctor = Doctor.objects.get(user=user)
                if doctor.is_verified:
                    return render(request, 'index_doctor.html', {'user': user})
                return redirect('waitlist_doctor')
            except:
                return redirect('profile_completion_doctor')
        else:
            del request.session['user']
    return redirect('login')

def profile_completion(request):
    if request.session.has_key('user'):
        user = User.objects.get(id=request.session['user'])
        if user.role == 'doctor':
            if request.method == 'POST':
                specialization = request.POST['specialization']
                qualification = request.POST['qualification']
                fees = request.POST['fees']
                experience = request.POST['experience']
                is_profile_complete = True
                doctor = Doctor(user=user, specialization=specialization, qualification=qualification, fees=fees, experience=experience, is_profile_complete=is_profile_complete)
                doctor.save()
                return redirect('index_doctor')
            else: # GET
                try:
                    doctor = Doctor.objects.get(user=user)
                    if doctor.is_profile_complete:
                        return redirect('index_doctor')
                except:
                    return render(request, 'profile_completion_doctor.html', {'user': user})
        else:
            del request.session['user']
    return redirect('login')

def waitlist(request):
    return render(request, 'waitlist_doctor.html')