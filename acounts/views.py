from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignUpForm

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully!")
            return redirect("acounts:sign_in")
    else:
        form = SignUpForm()
    
    context = {
        "form": form,
        "submit": "Sign Up",
        "error_message": "Please correct the errors below" if form.errors else None
    }
    return render(request, 'apps/acounts/forms.html', context)

def sign_in(request):
    # Show empty form on GET request
    if request.method == "GET":
        form = AuthenticationForm()
        context = {
            "form": form,
            "submit": "Sign In"
        }
        return render(request, "apps/acounts/forms.html", context)
    
    # Handle form submission on POST
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Use the cleaned data from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect("vsi:dashboard")
        
        # If form is invalid or authentication failed
        context = {
            "form": form,
            "submit": "Sign In",
            "error_message": "Invalid username or password"
        }
        return render(request, "apps/acounts/forms.html", context)
    