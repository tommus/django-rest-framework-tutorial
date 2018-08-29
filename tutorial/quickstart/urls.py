from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tutorial.quickstart import views

# region Application Name

app_name = "quickstart"

# endregion

# region Patterns

urlpatterns = [
    path("", views.UserList.as_view(), name="user_list"),
    path("u<int:pk>/", views.UserDetails.as_view(), name="user_details")
]

urlpatterns += format_suffix_patterns(urlpatterns)

# endregion
