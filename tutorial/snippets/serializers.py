from rest_framework import serializers

from tutorial.snippets.models import Snippet


# region Snippet

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet
        fields = ("id", "title", "code", "linenos", "language", "style", "owner")

# endregion
