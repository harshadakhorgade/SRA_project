from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, api_views

urlpatterns = [
    # Web (HTML views)
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    # path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("dashboard/", views.dashboard_redirect, name="dashboard_redirect"),

    # API (Flutter will use these)
    path("api/register/", api_views.RegisterAPIView.as_view(), name="api-register"),
    path("api/users/", api_views.UserListView.as_view(), name="api-user-list"),
    path("api/profile/", api_views.ProfileView.as_view(), name="api-profile"),
]
