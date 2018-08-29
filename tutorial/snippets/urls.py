from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tutorial.snippets import views

# region Application Name

app_name = "snippets"

# endregion

# region Patterns

urlpatterns = [
    path("", views.SnippetList.as_view(), name="snippet_list"),
    path("<int:pk>/", views.SnippetDetails.as_view(), name="snippet_details"),
]

urlpatterns += format_suffix_patterns(urlpatterns)

# endregion
