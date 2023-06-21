from django.shortcuts import render, redirect
from life_saver_user_auth.models import User
from life_saver_patient.models import Patient

def index(request):
    if request.session.has_key('user'):
        user = User.objects.get(id=request.session['user'])
        if user.role == 'patient':
            try:
                patient = Patient.objects.get(user=user)
                user = { user, patient }
                return render(request, 'index_patient.html', {'user': user})
            except:
                return redirect('profile_completion_patient')
        else:
            del request.session['user']
    return redirect('login')

def profile_completion(request):
    if request.session.has_key('user'):
        user = User.objects.get(id=request.session['user'])
        if user.role == 'patient':
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
            del request.session['user']
    return redirect('login')