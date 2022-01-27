
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Review system model
class Review(models.Model):
    
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000, null=False, blank=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review on {self.product.name} by {self.user}"

    class Meta:
        ordering = ['id']
