from django.contrib import admin

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import handler404
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='api'),   
    path('', include('main.urls'), name='main')   

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,  document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
