from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

def login_register_view(request):
    if request.method == 'POST':
        if 'Login' in request.POST:
            # Process login form data
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user is not None:
                return redirect('spotify_homepage_dummy:home')
            else:
                messages.error(request, "Invalid username or password!")
                return HttpResponseRedirect(reverse('user_auth:login_register_view'))

        elif 'Register' in request.POST:
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            # Process registration form data

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken. Please choose a different one.')
                return render(request, 'authentication/login-register.html')  # Redirect back to the login/register page

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email address already registered.')
                return render(request, 'authentication/login-register.html')   # Redirect back to the login/register page

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('spotify_homepage_dummy:home') # Redirect back to the login page after successful registration

    # If the request method is GET, render the login/register form
    return render(request, 'authentication/login-register.html')