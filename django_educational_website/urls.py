from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from . import settings

description = 'Educational website developed with Django and Rest Framework by Mahdi Malvandi. Project code source link:' \
              '<a href="https://github.com/MahdiMalvandi/django_educational">soruce code</a>' \
              'Visit my GitHub to see my other portfolios.' \
              'My GitHub:<a href="https://github.com/MahdiMalvandi">my github</a>'

schema_view = get_schema_view(
    openapi.Info(
        title="Django Educational Project",
        default_version='v1',
        description=description
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('users.urls', "users"), namespace='users'), name='users'),
    path('', include(('categories.urls', "categories"), namespace='categories'), name='categories'),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
