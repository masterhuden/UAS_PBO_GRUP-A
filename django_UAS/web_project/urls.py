from django.contrib import admin
from django.urls import include, path
from . import views
from . import assets
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.index),
    path("admin/", admin.site.urls),
    path("login", views.login),
    path("masuk", views.masuk),
    path("error", views.error),
    path("kumpulform", views.kumpulform),
    path("konsultasi", views.konsultasi),
    path("jadwal", views.jadwal),
]
urlpatterns += staticfiles_urlpatterns()
