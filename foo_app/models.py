from django.db import models
from django.utils.text import slugify
import itertools


class Foo(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    text = models.TextField()

    def __unicode__(self):
        return self.name

    def as_json(self):
        return dict(
            id=self.id,
            name=self.name,
            slug=self.slug,
            text=self.text,
        )

    def save(self, *args, **kwargs):
        slug_candidate = slugify(self.name)
        iterator = itertools.count()
        while Foo.objects.filter(slug=slug_candidate).exists():
            slug_candidate = slugify(
               self.name + str(iterator.next())
            )
        self.slug = slug_candidate
        super(Foo, self).save(*args, **kwargs)
