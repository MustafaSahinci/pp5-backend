from django.db import models
from django.contrib.auth.models import User
from cars.models import Car


class Save(models.Model):
    """
    Save model, related to 'owner' and 'cars'.
    'owner' is a User instance and 'car' is a Car instance.
    'unique_together' makes sure a user can't save the same car twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(
        Car, related_name='saves', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'car']

    def __str__(self):
        return f'{self.owner} {self.car}'
