from django.conf.urls import url, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^autos/(?P<pk>[0-9]+)/$', SnippetDetail.as_view()),

]
urlpatterns += format_suffix_patterns(urlpatterns)
router = DefaultRouter()
router.register(r'mark', MarkViewSet)
router.register(r'seller', SellerViewSet)
router.register(r'auto', AutoViewSet)
urlpatterns += router.urls
