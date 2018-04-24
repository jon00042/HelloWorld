from django.shortcuts import render, redirect
from django.contrib import messages
from apps.travel_app.models import User

def index(request):
    return render(request, 'travel_app/index.html')

def planes(request):
    return render(request, 'travel_app/planes.html')

def trains(request):
    return render(request, 'travel_app/trains.html')

def automobiles(request):
    return render(request, 'travel_app/automobiles.html')

def boats(request):
    return render(request, 'travel_app/boats.html')

def login(request):
    if (request.method == 'GET'):
        if ('user_id' in request.session):
            return redirect('travel_app:index')
        return render(request, 'travel_app/login.html')
    try:
        user = User.objects.get(email=request.POST['email'])
        if (user.password == request.POST['password']):
            request.session['user_id'] = user.id
            request.session['email'] = user.email
            return redirect('travel_app:index')
    except:
        pass
    messages.error(request, 'login attempt failed!')
    return redirect('travel_app:login')

def logout(request):
    request.session.clear()
    return redirect('travel_app:index')

def registration(request):
    if (request.method == 'GET'):
        if ('user_id' in request.session):
            return redirect('travel_app:index')
        return render(request, 'travel_app/registration.html')
    if (len(request.POST['email']) > 0 and len(request.POST['password']) > 0 and request.POST['password'] == request.POST['confirm']):
        try:
            user = User.objects.create(email=request.POST['email'], password=request.POST['password'])
            request.session['user_id'] = user.id
            request.session['email'] = user.email
            return redirect('travel_app:index')
        except:
            messages.error(request, 'email already in use!')
    return redirect('travel_app:registration')

