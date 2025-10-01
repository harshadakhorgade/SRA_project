from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_home(request):
    print("DEBUG: dashboard_home view called")  # 👈 add this
    return render(request, "dashboard/dashboard.html")