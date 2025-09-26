from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Factsheet

@admin.register(Factsheet)
class FactsheetAdmin(admin.ModelAdmin):
    list_display = ("id", "file_no", "name_of_society", "date_of_acceptance", "created_at")
    search_fields = ("file_no", "name_of_society", "developer_with_address")
    list_filter = ("date_of_acceptance", "created_at")
    readonly_fields = ("created_at",)

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "file_no",
                "name_of_society",
                "developer_with_address",
                "architect_with_address",
                "date_of_acceptance",
                "common_consent",
                "village_cts_no",
                "ownership_of_land",
                "area_of_plot",
            )
        }),
        ("D.P. Reservation Details", {
            "fields": (
                "buildable_reservation_name",
                "buildable_reservation_area",
                "non_buildable_reservation_name",
                "non_buildable_reservation_area",
                "slum_declared_or_censused",
            )
        }),
        ("Annexure II", {
            "fields": (
                "competent_authority_name",
                "certification_date",
            )
        }),
        ("Meta", {"fields": ("created_at",)}),
    )
