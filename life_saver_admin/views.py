from django.shortcuts import render, redirect
from life_saver_user_auth.models import User

def index(request):
    if request.session.has_key('user'):
        user = User.objects.get(id=request.session['user'])
        return render(request, 'index_admin.html', {'user': user})
    return redirect('login')
