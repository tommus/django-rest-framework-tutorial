from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# region Api Root

@api_view(http_method_names=["GET"])
def api_root(request, format=None):
    return Response({
        "users": reverse("quickstart:user_list", request=request, format=format),
        "snippets": reverse("snippets:snippet_list", request=request, format=format),
    })


# endregion

# region Patterns

urlpatterns = [
    path("", api_root),
    path("users/", include("tutorial.quickstart.urls", namespace="quickstart")),
    path("snippets/", include("tutorial.snippets.urls", namespace="snippets")),
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]

# endregion
