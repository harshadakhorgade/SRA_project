from django.contrib import admin
from .models import Factsheet, AnnexureII, AnnexureIII, TransitCamp, Approval, ConstructionStatus, StopWork

@admin.register(Factsheet)
class FactsheetAdmin(admin.ModelAdmin):
    list_display = ("id", "file_no", "name_of_society", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    search_fields = ("file_no", "name_of_society")
    list_filter = ("created_at", "updated_at")


@admin.register(AnnexureII)
class AnnexureIIAdmin(admin.ModelAdmin):
    list_display = ("id", "competent_authority", "tenants_total", "tenants_eligible")
    search_fields = ("competent_authority",)


@admin.register(AnnexureIII)
class AnnexureIIIAdmin(admin.ModelAdmin):
    list_display = ("id", "certification_date_annexure3", "fsi_sanctioned", "rehab_built_up_area")
    search_fields = ("certification_date_annexure3",)


@admin.register(TransitCamp)
class TransitCampAdmin(admin.ModelAdmin):
    list_display = ("id", "building_no", "floors", "no_of_tenants", "date_of_approval")


@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    list_display = ("id", "building_type", "building_no", "ioa_date", "remarks")


@admin.register(ConstructionStatus)
class ConstructionStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "building_type", "building_no", "date_of_visit", "no_of_floors_completed")


@admin.register(StopWork)
class StopWorkAdmin(admin.ModelAdmin):
    list_display = ("id", "building_no", "date_of_order", "reason")
