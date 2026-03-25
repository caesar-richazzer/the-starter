from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages

def home_view(request):
    return render(request, 'home.html')
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # SUCCESS: Save the new account to the database
            user = form.save() 
            
            # This is where the error was! 
            # We now pass the 'user' we just created into the login function.
            login(request, user) 
            
            messages.success(request, f"Welcome to Sokoni Pro, {user.username}!")
            return redirect('home')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})