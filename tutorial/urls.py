from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("accounts/", include("tutorial.quickstart.urls")),
    path("snippets/", include("tutorial.snippets.urls")),
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]
