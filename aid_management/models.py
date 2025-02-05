from django.db import models
from django.conf import settings

class AidRecipients(models.Model):
    
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='userid')
    aid_id = models.CharField(primary_key=True, max_length=10)  # Primary Key
    app = models.ForeignKey('home.Application', on_delete=models.CASCADE, related_name='aid_recipients')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='userid', related_name='user_aid_recipients')

    AID_STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Suspended', 'Suspended'),
        ('Cancelled', 'Cancelled'),
        ('Concluded', 'Concluded'),
    ]
    aid_status = models.CharField(max_length=10, choices=AID_STATUS_CHOICES)

    AID_TYPE_CHOICES = [
        ('Financial', 'Financial'),
        ('Tuition Reduction', 'Tuition Reduction'),
        ('Food', 'Food'),
        ('Study Supplies', 'Study Supplies'),
        ('Miscellaneous', 'Miscellaneous'),
    ]
    aid_type = models.CharField(max_length=20, choices=AID_TYPE_CHOICES)

    aid_desc = models.TextField(max_length=1000)
    aid_changereason = models.TextField(max_length=1000, blank=True, null=True)
    aid_changedecider = models.CharField(max_length=10, blank=True, null=True)  # User ID of the one who changed it
    aid_changedate = models.DateField(blank=True, null=True)

    aid_startdate = models.DateField()
    aid_enddate = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.aid_id} - {self.aid_status}"

