from django.contrib.auth.models import User
from rest_framework import serializers

from tutorial.snippets.models import Snippet


# region User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ("id", "username", "snippets")

# endregion
