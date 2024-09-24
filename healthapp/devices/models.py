from django.db import models

class fda_data(models.Model):
    k_number = models.CharField(max_length=255, primary_key=True)
    manufacturer_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True, blank=True)
    country_code = models.CharField(max_length=3)
    zip_code = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    date_received = models.DateField(null=True, blank=True)
    decision_date = models.DateField(null=True, blank=True)
    decision_description = models.TextField(null=True, blank=True)
    product_code = models.CharField(max_length=50)
    statement_or_summary = models.TextField(null=True, blank=True)
    clearance_type = models.CharField(max_length=50, null=True, blank=True)
    third_party_flag = models.BooleanField(default=False)
    expedited_review_flag = models.BooleanField(default=False)
    device_name = models.CharField(max_length=255)
    url = models.URLField(max_length=200, null=True, blank=True)
    device_description = models.TextField(null=True, blank=True)
    medical_specialty_description = models.CharField(max_length=255, null=True, blank=True)
    device_class = models.CharField(max_length=50, null=True, blank=True)
    regulation_number = models.CharField(max_length=50, null=True, blank=True)
    submission_type_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.device_name
    
    class Meta:
        db_table = 'fda_data'

class eudamed_data(models.Model):
    basic_udi = models.CharField(max_length=255, primary_key=True)
    primary_di = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    ulid = models.CharField(max_length=255)
    basic_udi_di_data_ulid = models.CharField(max_length=255)
    risk_class = models.CharField(max_length=50, null=True, blank=True)
    device_name = models.CharField(max_length=255)
    manufacturer_name = models.CharField(max_length=255)
    manufacturer_srn = models.CharField(max_length=255, null=True, blank=True)
    device_status_type = models.CharField(max_length=255, null=True, blank=True)
    manufacturer_status = models.CharField(max_length=255, null=True, blank=True)
    latest_version = models.CharField(max_length=50, null=True, blank=True)
    version_number = models.CharField(max_length=50, null=True, blank=True)
    reference = models.CharField(max_length=255, null=True, blank=True)
    basic_udi_data_version_number = models.CharField(max_length=50, null=True, blank=True)
    container_package_count = models.IntegerField(null=True, blank=True)
    authorised_representative_srn = models.CharField(max_length=255, null=True, blank=True)
    authorised_representative_name = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.device_name
    
    class Meta:
        db_table = 'eudamed_data'