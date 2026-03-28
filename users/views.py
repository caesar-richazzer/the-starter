from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def home_view(request):
    """
    THE GATEKEEPER:
    If the user is logged in, they NEVER see the landing page.
    They are teleported instantly to the Market or Dashboard.
    """
    if request.user.is_authenticated:
        if request.user.is_freelancer:
            return redirect('seller-dashboard')
        else:
            return redirect('market') # Clients land here
    
    # ONLY guests (logged out) see the Arctic Crystal Landing Page
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log them in
            # Redirect to 'home', which now knows to send them to the Market
            return redirect('home') 
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
def profile_settings_view(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('home')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'users/profile_settings.html', {'p_form': p_form})



@login_required
def become_freelancer_view(request):
    if request.method == 'POST':
        user = request.user
        user.is_freelancer = True
        user.save()
        messages.success(request, "Hongera! You are now a Freelancer. Update your profile to start selling.")
        return redirect('profile-settings') # Redirects to settings page
    
    return render(request, 'users/become_freelancer.html')

@login_required
def login_redirect_view(request):
    """
    This view decides where to send the user immediately after they log in.
    """
    if request.user.is_freelancer:
        # If they are a seller, send them to their dashboard
        return redirect('seller-dashboard') 
    else:
        # If they are just a buyer, send them to the marketplace (home)
        return redirect('home')


def market_view(request):
    """ The Public/Client Market where Gigs are listed. """
    return render(request, 'users/market.html')

@login_required
def work_seeking_view(request):
    """ The Job Board where Freelancers find work. Restricted to Freelancers. """
    if not request.user.is_freelancer:
        # If a client tries to enter, send them back or show error
        return redirect('home') 
    
    return render(request, 'users/work_seeking.html')

@login_required
def post_auth_redirect(request):
    """ Smart Redirect after login """
    if request.user.is_freelancer:
        return redirect('seller-dashboard')
    else:
        return redirect('market')