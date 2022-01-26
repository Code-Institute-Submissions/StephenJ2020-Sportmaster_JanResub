""" Review Model """

from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):
<<<<<<< HEAD
    """ Review's Model """
    username = models.ForeignKey(
        User, related_name="reviews", on_delete=models.CASCADE,
        null=True, blank=True)
    products = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    review = models.TextField(max_length=500)

    def __str__(self):
        # return f"Review on {self.product.name} by {self.user}"
        return str(self.title)

    class Meta:
        ordering = ['id']
=======
    """
    Creates a review model to allow user to perform
    CRUD operations on product reviews
    """

    RATE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.IntegerField(choices=RATE)
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
>>>>>>> aebfb7de8b542e76a323e3985274197b850baa1b
