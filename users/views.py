from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Profile


# 🔹 User Registration (Django form-based)
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            role = form.cleaned_data["role"]

            if role == "coordinator":
                user.is_staff = True
            user.save()

            # Create profile automatically
            Profile.objects.get_or_create(user=user)

            login(request, user)
            messages.success(request, "Account created successfully!")

            return redirect("dashboard_redirect")  # 🔹 go to role-based dashboard
    else:
        form = CustomUserCreationForm()

    return render(request, "users/register.html", {"form": form})


# 🔹 Login (optional custom view; can also use Django’s built-in LoginView)
def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return redirect("dashboard_redirect")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "users/login.html")


# 🔹 Dashboard Redirect (role-based)
@login_required
def dashboard_redirect(request):
    user = request.user
    if user.is_superuser or user.is_staff:
        return redirect("admin_dashboard")
    elif hasattr(user, "role") and user.role == "coordinator":
        return redirect("coordinator_dashboard")
    else:
        return redirect("user_dashboard")


# 🔹 Logout
def user_logout(request):
    logout(request)
    return redirect("login")
