from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_factsheet, name="create-factsheet"),
    path("list/", views.factsheet_list, name="factsheet-list"),
    # path("<int:pk>/", views.factsheet_detail, name="factsheet-detail"),
]
