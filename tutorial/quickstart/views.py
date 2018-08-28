from django.contrib.auth.models import User
from rest_framework import generics

from tutorial.quickstart.serializers import UserSerializer


# region User

class UserList(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    """
    API endpoint that allows user to be viewed.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# endregion
