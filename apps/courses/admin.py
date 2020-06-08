from django.contrib import admin

from users.models import CustomUser
from .models import Course, Category, Answer, Question, Section


class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ['students']
    readonly_fields = ['teachers']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(teachers__in=[request.user])

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.teachers = request.user
        super().save_model(request, obj, form, change)
    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == "students":
    #         kwargs["queryset"] = CustomUser.objects.filter(is_student=True)
    #     elif db_field.name == 'teachers':
    #         kwargs["queryset"] = CustomUser.objects.filter(is_teacher=True)
    #     return super(CourseAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


class CategoryAdmin(admin.ModelAdmin):
    pass


class SectionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(course__teachers__in=[request.user])


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'section', ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(section__course__teachers__in=[request.user])


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
