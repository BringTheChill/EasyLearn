from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from courses.views import course_detail, course_add
from . import settings, views
from students.views import student_detail

urlpatterns = [
    path('filer/', include('filer.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('courses/', include('courses.urls')),
    path('student_detail/', student_detail, name="student_detail"),
    # path('', include('cms.urls')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
