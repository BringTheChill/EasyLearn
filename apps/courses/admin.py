from django.contrib import admin

from users.models import CustomUser
from .models import Course, Category, Answer, Question, Section


class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ['students']
    readonly_fields = ['teachers']

    # Afisam in admin doar cursurile profesorului respectiv
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(teachers__in=[request.user])

    # Salvam ca 'teacher' al cursului pe cel care creeaza cursul
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.teachers = request.user
        super().save_model(request, obj, form, change)


class CategoryAdmin(admin.ModelAdmin):
    pass


class SectionAdmin(admin.ModelAdmin):
    # Afisam in admin doar 'section'-urile profesorului respectiv
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(course__teachers__in=[request.user])

    # Pentru a afisa in admin doar cursurile din cursurile profesorului
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.related_model:
            kwargs["queryset"] = db_field.related_model.objects.filter(section__course__teachers__in=[request.user])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'section']

    # Afisam in admin doar intrebarile profesorului respectiv
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(section__course__teachers__in=[request.user])

    # Pentru a afisa in admin doar capitolele din cursurile profesorului
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.related_model:
            kwargs["queryset"] = db_field.related_model.objects.filter(course__teachers__in=[request.user])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'question']

    # Afisam in admin doar raspunsurile profesorului respectiv
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(question__section__course__teachers__in=[request.user])

    # Pentru a afisa in admin doar capitolele din cursurile profesorului
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.related_model:
            kwargs["queryset"] = db_field.related_model.objects.filter(section__course__teachers__in=[request.user])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
