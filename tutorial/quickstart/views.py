from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


# region User

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users be be viewed and edited.
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


# endregion

# region Group

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed and edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# endregion
