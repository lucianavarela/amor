
from django.conf.urls import url
from django.contrib import admin
from wedding import views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', views.index),
]
