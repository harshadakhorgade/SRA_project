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
    competent_authority_name = models.CharField(max_length=255, blank=True, null=True)
    certification_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Factsheet - {self.file_no}"
