from django.urls import path
from . import views


app_name = "dashboard"   # 👈 important for namespacing

urlpatterns = [
    path("working/", views.working_test, name="working"),  # Completely isolated test
    path("test/", views.test_view, name="test"),  # Add a test URL
    path("simple/", views.simple_dashboard, name="simple"),  # Simple test without login
    path("", views.dashboard_home, name="home"),  # Move this to last
]