from django.conf.urls import url
from core import views
urlpatterns = [
     url(r'^$', views.main),
     url(r'^seller/$', views.seller),
     url(r'^technical_inspection/$', views.technical_inspection),
     url(r'^new_auto/$', views.new_auto),
]