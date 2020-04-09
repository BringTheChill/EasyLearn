from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from courses.views import course_detail, course_add
from . import settings, views

urlpatterns = [
    path('filer/', include('filer.urls')),
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    # path('', include('cms.urls')),
    path('', views.index, name='index'),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
