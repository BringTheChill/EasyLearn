from django.db import models
from filer.fields.image import FilerImageField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    image = FilerImageField(null=True, blank=False, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name="courses")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="price")

    def get_absolute_url(self):
        return reverse('course_detail', args=(self.id,))

    def __str__(self):
        return self.name
