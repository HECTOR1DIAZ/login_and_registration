from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^submit$',views.submit),
    url(r'^welcome$', views.welcome),
    url(r'^welcome/(?P<id>\d+)$',views.welcome),

]