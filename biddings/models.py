from django.db import models
from django.contrib.auth.models import User
from cars.models import Car


class Bidding(models.Model):
    """
    Bidding model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
