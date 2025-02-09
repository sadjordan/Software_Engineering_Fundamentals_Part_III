from django.db import models

class UserIDTracker(models.Model):
    category = models.CharField(max_length=1, unique=True)  # M, F, S, U
    last_number = models.IntegerField(default=0)

    @staticmethod
    def generate_user_id(category):
        tracker, _ = UserIDTracker.objects.get_or_create(category=category)
        tracker.last_number += 1
        tracker.save()
        return f"{category}{tracker.last_number:09d}"