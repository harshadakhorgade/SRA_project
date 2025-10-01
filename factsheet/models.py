from django.db import models

# ----------------- FactSheet -----------------
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

    # timestamps 👇
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.file_no} - {self.name_of_society}"


# ----------------- Annexure II -----------------
class AnnexureII(models.Model):
    factsheet = models.OneToOneField(Factsheet, on_delete=models.CASCADE)

    competent_authority = models.CharField(max_length=255, blank=True, null=True)
    certification_date_annexure2 = models.DateField(null=True, blank=True)
    tenants_total = models.IntegerField(null=True, blank=True)
    tenants_eligible = models.IntegerField(null=True, blank=True)
    tenants_residential = models.IntegerField(null=True, blank=True)
    tenants_commercial = models.IntegerField(null=True, blank=True)
    tenants_res_comm = models.IntegerField(null=True, blank=True)
    tenants_others = models.IntegerField(null=True, blank=True)
    tenants_pap = models.IntegerField(null=True, blank=True)
    tenants_non_eligible = models.IntegerField(null=True, blank=True)
    percent_eligible_consent = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Annexure II for {self.factsheet.file_no}"


# ----------------- Annexure III -----------------
class AnnexureIII(models.Model):
    factsheet = models.OneToOneField(Factsheet, on_delete=models.CASCADE)

    certification_date_annexure3 = models.CharField(max_length=255, blank=True, null=True)
    date_of_bank_guarantee = models.CharField(max_length=255, blank=True, null=True)
    amount_bank_guarantee = models.CharField(max_length=255, blank=True, null=True)
    land_premium_amount = models.CharField(max_length=255, blank=True, null=True)
    revised_loi_details = models.CharField(max_length=255, blank=True, null=True)
    loi_issue_details = models.CharField(max_length=255, blank=True, null=True)
    fsi_sanctioned = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    rehab_built_up_area = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    pap_generated = models.IntegerField(null=True, blank=True)
    permissible_sale_builtup_area = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    tdr_generated = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    tdr_granted_date = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Annexure III for {self.factsheet.file_no}"


# ----------------- Transit Camps -----------------
class TransitCamp(models.Model):
    building_no = models.CharField(max_length=100)
    floors = models.CharField(max_length=100, blank=True, null=True)
    no_of_tenants = models.IntegerField(blank=True, null=True)
    date_of_approval = models.DateField(blank=True, null=True)
    status_on_visit = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Transit Camp {self.building_no}"


# ----------------- Approval (Rehab / Layout / Sale) -----------------
class Approval(models.Model):
    BUILDING_TYPES = [
        ('rehab', 'Rehab'),
        ('layout', 'Layout'),
        ('sale', 'Sale'),
    ]

    building_type = models.CharField(max_length=20, choices=BUILDING_TYPES)
    building_no = models.CharField(max_length=100)
    ioa_date = models.DateField(blank=True, null=True)
    no_of_floors = models.CharField(max_length=100, blank=True, null=True)
    no_of_tenants = models.CharField(max_length=100, blank=True, null=True)
    date_of_plinth_cc = models.DateField(blank=True, null=True)
    date_of_further_cc = models.DateField(blank=True, null=True)
    date_of_full_cc = models.DateField(blank=True, null=True)
    date_of_lottery = models.DateField(blank=True, null=True)
    date_of_part_oc = models.DateField(blank=True, null=True)
    date_of_full_oc = models.DateField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_building_type_display()} - {self.building_no}"


# ----------------- Construction Status -----------------
class ConstructionStatus(models.Model):
    BUILDING_TYPES = [
        ('rehab', 'Rehab'),
        ('sale', 'Sale'),
    ]

    building_type = models.CharField(max_length=20, choices=BUILDING_TYPES)
    building_no = models.CharField(max_length=100)
    date_of_visit = models.DateField(blank=True, null=True)
    no_of_floors_sanctioned = models.IntegerField(blank=True, null=True)
    no_of_floors_completed = models.IntegerField(blank=True, null=True)
    no_of_tenants_sanctioned = models.IntegerField(blank=True, null=True)
    no_of_tenants_completed = models.IntegerField(blank=True, null=True)
    reasons_for_delay = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_building_type_display()} Status - {self.building_no}"


# ----------------- Stop Work -----------------
class StopWork(models.Model):
    building_no = models.CharField(max_length=100)
    date_of_order = models.DateField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Stop Work - {self.building_no}"
