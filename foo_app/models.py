from django.db import models
from django.utils.text import slugify


class Foo(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
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
        self.slug = slugify(self.name)
        super(Foo, self).save(*args, **kwargs)