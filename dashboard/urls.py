from django.urls import path
from . import views


app_name = "dashboard"   # 👈 important for namespacing

urlpatterns = [
    path("", views.dashboard_home, name="home"),
]