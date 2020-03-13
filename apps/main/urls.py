from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings
from .views import index

urlpatterns = [
    path('filer/', include('filer.urls')),
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('', include('cms.urls')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
