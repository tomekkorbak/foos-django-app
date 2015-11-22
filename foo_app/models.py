from django.db import models


class Foo(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    text = models.TextField()

    def __unicode__(self):
        return self.name

    def as_json(self):
        return dict(
            name=self.name,
            slug=self.slug,
            text=self.text,
        )