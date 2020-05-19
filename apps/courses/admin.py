from django.contrib import admin

from users.models import CustomUser
from .models import Course, Category, Answer, Question, Section


class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ['students', 'teachers']

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == "students":
    #         kwargs["queryset"] = CustomUser.objects.filter(is_student=True)
    #     elif db_field.name == 'teachers':
    #         kwargs["queryset"] = CustomUser.objects.filter(is_teacher=True)
    #     return super(CourseAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


class CategoryAdmin(admin.ModelAdmin):
    pass


class SectionAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
