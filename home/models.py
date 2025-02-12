from django.db import models
from Login.models import User
from django.conf import settings

class Application(models.Model):
    APP_TYPE_CHOICES = [
        ("Financial", "Financial"),
        ("Tuition Reduction", "Tuition Reduction"),
        ("Food", "Food"),
        ("Study Supplies", "Study Supplies"),
        ("Miscellaneous", "Miscellaneous"),
    ]

    APP_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Denied", "Denied"),
        ("Appealing", "Appealing"),
    ]

    Financial_aid_STATUS_CHOICES = [
        ("Waiting for Approval", "Waiting for Approval"),
        ("Approved", "Approved"),
        ("Denied", "Denied"),
        ("Verified", "Verified"),
    ]



    app_id = models.CharField(max_length=10, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='userid')
    app_type = models.CharField(max_length=20, choices=APP_TYPE_CHOICES)
    app_date = models.DateField()
    app_description = models.TextField(max_length=1000)
    
    app_attached1 = models.BinaryField(null=True, blank=True)
    app_attached2 = models.BinaryField(null=True, blank=True)
    app_attached3 = models.BinaryField(null=True, blank=True)
    app_attached4 = models.BinaryField(null=True, blank=True)
    app_attached5 = models.BinaryField(null=True, blank=True)

    app_status = models.CharField(max_length=10, choices=APP_STATUS_CHOICES, default="Pending")
    forwarded_to_finance = models.BooleanField(default=False)
    Financial_aid_status = models.CharField(max_length=20, choices=Financial_aid_STATUS_CHOICES, default="Waiting for Approval")
    
    app_denyreason = models.TextField(max_length=1000, blank=True, null=True)
    app_denyreason2 = models.TextField(max_length=1000, blank=True, null=True)
    app_appeal = models.TextField(max_length=1000, blank=True, null=True)
    app_appealdate = models.DateField(blank=True, null=True)
    
    app_decider = models.CharField(max_length=10, blank=True, null=True)
    app_decider2 = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"Application {self.app_id} - {self.app_type} ({self.app_status})"
