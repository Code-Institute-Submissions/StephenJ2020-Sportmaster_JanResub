from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
<<<<<<< HEAD
        'username',
        'products',
        'created',
        'updated',
        # 'title',
        'review',
=======
        'title',
        'product',
        'user',
        'rating',
        'review_date'
>>>>>>> aebfb7de8b542e76a323e3985274197b850baa1b
    )
