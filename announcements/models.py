from django.db import models
from profiles.models import UserProfile


class Announcements(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Post(models.Model):
    announcements = models.ForeignKey(Announcements, related_name="posts",
                                      on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    author = models.CharField(max_length=100)
    intro = models.TextField(max_length=1000, null=False,
                             blank=False)
    blurb = models.TextField(max_length=3000, null=False,
                             blank=False)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
