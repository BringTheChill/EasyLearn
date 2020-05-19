from django.db import models
from django.urls import reverse

from main import settings
# from students.models import StudentUser
# from teachers.models import TeacherUser

from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser
from users.models import CustomUser

# Start Trying something new


# class User(AbstractBaseUser, PermissionsMixin):
#     is_student = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name="students")

    # quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    # interests = models.ManyToManyField(Subject, related_name='interested_students')
    def __str__(self):
        return self.user.get_full_name()


# End
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
    #price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="price")

    students = models.ManyToManyField(CustomUser, related_name='students_to_courses',
                                      limit_choices_to={'is_student': True})
    teachers = models.ManyToManyField(CustomUser, related_name='teachers_to_courses',
                                      limit_choices_to={'is_teacher': True})

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
        unique_together = ('course', 'number',)

    def __str__(self):
        return self.title

    def get_test_url(self):
        return reverse('do_test', args=(self.id,))

    def get_absolute_url(self):
        return reverse('do_section', args=(self.id,))

    def get_next_section_url(self):
        next_section = Section.objects.get(number=self.number + 1)
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
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="user_answers")

    class Meta:
        unique_together = ('question', 'user',)
