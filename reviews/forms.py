from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Create a form for users to add reviews
    """
    class Meta:
        model = Review
        fields = ('review',)
