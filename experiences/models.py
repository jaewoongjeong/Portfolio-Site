from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager


# Create your models here.
class PostModel(models.Model):
    POST_TYPES = (
        ('PR', 'Project'),
        ('EX', 'Experience'),
    )
    type = models.CharField(max_length=2, choices=POST_TYPES)
    position = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    content = models.TextField(null=True)
    tags = TaggableManager(blank=True)

    slug = models.SlugField(unique=True, max_length=50, allow_unicode=True)

    def __str__(self):
        return self.place

    def get_absolute_url(self):
        return reverse('experiences:post', args=(self.slug,))