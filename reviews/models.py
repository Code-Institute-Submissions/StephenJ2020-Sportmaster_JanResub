from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(null=False, blank=False, default='')
    review_date = models.DateTimeField(auto_now_add=True)
