from django.conf.urls import url
from updater import views
urlpatterns = [
     url(r'^home/$', views.update_auto),

]