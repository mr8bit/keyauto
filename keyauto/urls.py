from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from core import urls as core_urls
from api import urls as api_urls
from updater import urls as updater_urls
urlpatterns = [
     url(r'^admin/', admin.site.urls),
     url(r'^api/', include(api_urls)),
     url(r'^updater/', include(updater_urls)),
     url(r'^', include(core_urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)