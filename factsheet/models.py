from django.db import models

# Create your models here.
from django.db import models

class Factsheet(models.Model):
    # Basic Info
    file_no = models.CharField(max_length=200)
    name_of_society = models.CharField(max_length=255)
    developer_with_address = models.TextField()
    architect_with_address = models.TextField()
    date_of_acceptance = models.DateField()
    common_consent = models.CharField(max_length=255)
    village_cts_no = models.TextField()
    ownership_of_land = models.CharField(max_length=100)
    area_of_plot = models.CharField(max_length=100)

    # D.P. Reservation Details
    buildable_reservation_name = models.CharField(max_length=255, blank=True, null=True)
    buildable_reservation_area = models.CharField(max_length=100, blank=True, null=True)
    non_buildable_reservation_name = models.CharField(max_length=255, blank=True, null=True)
    non_buildable_reservation_area = models.CharField(max_length=100, blank=True, null=True)
    slum_declared_or_censused = models.CharField(max_length=255, blank=True, null=True)

    # Annexure II
    competent_authority = models.CharField(max_length=255, blank=True)
    certification_date_annexure2 = models.DateField(null=True, blank=True)
    tenants_total = models.IntegerField(null=True, blank=True)
    tenants_eligible = models.IntegerField(null=True, blank=True)
    tenants_residential = models.IntegerField(null=True, blank=True)
    tenants_commercial = models.IntegerField(null=True, blank=True)
    tenants_res_comm = models.IntegerField(null=True, blank=True)
    tenants_others = models.IntegerField(null=True, blank=True)
    tenants_pap = models.IntegerField(null=True, blank=True)
    tenants_non_eligible = models.IntegerField(null=True, blank=True)
    percent_eligible_consent = models.CharField(max_length=255, blank=True)

    # Annexure III
    certification_date_annexure3 = models.CharField(max_length=255, blank=True)
    date_of_bank_guarantee = models.CharField(max_length=255, blank=True)
    amount_bank_guarantee = models.CharField(max_length=255, blank=True)
    land_premium_amount = models.CharField(max_length=255, blank=True)
    revised_loi_details = models.CharField(max_length=255, blank=True)
    loi_issue_details = models.CharField(max_length=255, blank=True)
    fsi_sanctioned = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    rehab_built_up_area = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    pap_generated = models.IntegerField(null=True, blank=True)
    permissible_sale_builtup_area = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    tdr_generated = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    tdr_granted_date = models.CharField(max_length=255, blank=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"FactSheet {self.file_no}"

 