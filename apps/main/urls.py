from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework import routers

import courses
# from courses.views import SectionViewSet
from . import settings, views
from students.views import student_detail

from courses.viewss import classroom, students, teachers


# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'sections', SectionViewSet)

urlpatterns = [
    path('filer/', include('filer.urls')),
    path('admin/', admin.site.urls),
    # path('register/', student_views.register, name='register'),
    path('', views.index, name='index'),
    # path('', include('django.contrib.auth.urls')),
    # path('api/', include(router.urls)),
    path('contact/', include('contact.urls')),
    path('courses/', include('courses.urls')),
    path('student_detail/', student_detail, name="student_detail"),
    # path('', include('cms.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('search/',  include("watson.urls", namespace="watson")),
    path('ratings/',  include('star_ratings.urls', namespace='ratings')),

]

admin.site.site_header = "EasyLearn Dashboard"
admin.site.site_title = "EasyLearn"
admin.site.index_title = "Welcome to EasyLearn"

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
