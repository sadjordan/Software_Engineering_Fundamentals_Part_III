from django.db import models

class FinanceInformation(models.Model):
    current_sem_budget = models.DecimalField(
        max_digits=12, decimal_places=2, help_text="Current semester aid budget in MYR"
    )
    total_aid_balance = models.DecimalField(
        max_digits=12, decimal_places=2, help_text="Total aid account balance in MYR"
    )
    
    most_recent_subtraction = models.DecimalField(
        max_digits=12, decimal_places=2, help_text="temporary storage of last transaction"
    )

    last_updated = models.DateTimeField(auto_now=True, help_text="Last updated timestamp")

    def __str__(self):
        return f"Finance Info - {self.last_updated.strftime('%Y-%m-%d %H:%M:%S')}"