from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tutorial.snippets import views

urlpatterns = [
    path("", views.SnippetList.as_view()),
    path("<int:pk>/", views.SnippetDetails.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)
