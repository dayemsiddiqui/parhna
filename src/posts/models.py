from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length =120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    # slug = models.SlugField(max_length =120)
    category = models.ForeignKey('posts.Category')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id":self.id})

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_post_category', kwargs = { 'slug': self.slug })
