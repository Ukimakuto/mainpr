from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserLoginForm
# views.py
# takes http requests and returns http response, like HTML documents.
def userlogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'homepage.html')

def lec_one(request):
    if request.user.is_authenticated:
        return render(request, 'prog1lec.html')
    else:
        return redirect('login')


def lec_two(request):
    if request.user.is_authenticated:
        return render(request, 'prog2lec.html')
    else:
        return redirect('login')

def home(request):
    return render(request, 'homepage.html')

def userlogout(request):
    logout(request)
    return redirect('login')
