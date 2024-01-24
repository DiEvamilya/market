from uuid import uuid4

from django.db import models, IntegrityError
from django.utils.text import slugify

from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f' {self.name}-{self.category}')

        while True:
            try:
                super().save(*args, **kwargs)
                break
            except IntegrityError:
                self.slug = f'{self.slug}-{str(uuid4())[:8]}'
        return super().save()
