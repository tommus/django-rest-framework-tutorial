from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("groups", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("snippets/", include("tutorial.snippets.urls")),
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]
