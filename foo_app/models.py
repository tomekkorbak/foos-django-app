from django.db import models

class Foo(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    text = models.TextField()