from django.shortcuts import render, redirect
from life_saver_user_auth.forms import UserForm
from life_saver_user_auth.models import User

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email, password=password)
            request.session['user'] = user.id
            if user.role == 'admin':
                return redirect('index_admin')
            elif user.role == 'patient':
                return redirect('index_patient')
            elif user.role == 'doctor':
                return redirect('index_doctor')
        except:
            return render(request, 'login.html', {'error': 'Invalid Email or Password'})
    return render(request, 'login.html')

def register(request):
    user = UserForm(request.POST or None)
    if user.is_valid():
        user.save()
        return redirect('login')
    elif user.errors:
        return render(request, 'register.html', {'error': user.errors})
    return render(request, 'register.html')

def logout(request):
    del request.session['user']
    return redirect('login')