from django.db import models
from django.conf import settings
from properties.models import Property


class Payment(models.Model):

    PAYMENT_STATUS = (
        ('INITIATED', 'Initiated'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    property = models.OneToOneField(
        Property,
        on_delete=models.CASCADE,
        related_name='payment'
    )

    amount = models.DecimalField(max_digits=8, decimal_places=2)

    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS,
        default='INITIATED'
    )

    transaction_id = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property.title} - {self.payment_status}"




