from django.db import models
from filer.fields.image import FilerImageField
from django.urls import reverse

from main import settings
from students.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    file = models.ImageField(null=True, blank=False, verbose_name="image")
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name="courses")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="price")
    students = models.ManyToManyField(User)

    def get_absolute_url(self):
        return reverse('course_detail', args=(self.id,))

    def __str__(self):
        return self.name


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    video = models.FileField(upload_to='videos/', null=True, verbose_name="")

    class Meta:
        unique_together = ('course', 'number', )

    def __str__(self):
        return self.title

    def get_test_url(self):
        return reverse('do_test', args=(self.id,))

    def get_absolute_url(self):
        return reverse('do_section', args=(self.id, ))

    def get_next_section_url(self):
        next_section = Section.objects.get(number=self.number+1)
        return reverse('do_section', args=(next_section.id,))


class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    text = models.CharField(max_length=1000)
    correct = models.BooleanField()

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('question', 'user', )
