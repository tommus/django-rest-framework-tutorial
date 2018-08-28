from rest_framework import generics
from rest_framework import permissions

from tutorial.snippets.models import Snippet
from tutorial.snippets.permissions import IsOwnerOrReadOnly
from tutorial.snippets.serializers import SnippetSerializer


# region Snippet - List & Create

class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# endregion

# region Snippet - Details & Edit & Delete

class SnippetDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

# endregion
