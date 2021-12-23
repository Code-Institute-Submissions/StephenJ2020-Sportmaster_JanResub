from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from .models import Review
from .forms import ProductReview

# Create your views here


def reviews(request):
    """ A view to return the review page """
    reviews = Review.objects.order_by('-date_created')
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/reviews.html', context)


@login_required
def product_review(request):
    """A view to allow users to write their own reviews
    and add them to the site.
    """
    if request.method == 'POST':
        form = ProductReview(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.creator = UserProfile.objects.get(user=request.user)
            form.save()
            messages.success(request, 'Review added!')
            return redirect('reviews')
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductReview()

    template = 'reviews/product_review.html'
    context = {
        'form': form
    }
    return render(request, template, context)
