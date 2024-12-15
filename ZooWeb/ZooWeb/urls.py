
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from ZooWeb import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('realtyestateapp.urls', namespace='realtyestateapp')),
    path('catalog/', include('goods.urls', namespace='catalog')),
    path('user/', include('users.urls', namespace='user')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
