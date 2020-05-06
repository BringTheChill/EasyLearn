from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework import routers

from . import settings, views
from students.views import student_detail
from api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('filer/', include('filer.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('courses/', include('courses.urls')),
    path('student_detail/', student_detail, name="student_detail"),
    # path('', include('cms.urls')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
