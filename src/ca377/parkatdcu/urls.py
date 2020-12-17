from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'parkatdcu'

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^carparks/', views.carparks, name="carparks"),
]

urlpatterns += staticfiles_urlpatterns()
