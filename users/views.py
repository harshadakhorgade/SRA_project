from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import Profile

# 🔹 User Registration
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # Create profile automatically
            Profile.objects.get_or_create(user=user)

            messages.success(request, "Account created successfully! Please login below.")
            form = CustomUserCreationForm()
            return render(request, "users/register.html", {"form": form})
    else:
        form = CustomUserCreationForm()

    return render(request, "users/register.html", {"form": form})

# 🔹 Login view
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import EmailAuthenticationForm

def user_login(request):
    if request.method == "POST":
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("DEBUG: User logged in ✅")
            return redirect("dashboard:home")  # redirect to dashboard
        else:
            messages.error(request, "Invalid email or password")
            print("DEBUG: Login errors:", form.errors)
    else:
        form = EmailAuthenticationForm()

    return render(request, "users/login.html", {"form": form})

# 🔹 Dashboard redirect (simplified)
@login_required
def dashboard_redirect(request):
    if request.user.is_staff or request.user.is_superuser:
        return redirect("/admin/")  # Admin goes to admin panel
    else:
        return redirect("dashboard:home")  # Regular user goes to dashboard

# 🔹 Logout
def user_logout(request):
    logout(request)
    return redirect("login")
