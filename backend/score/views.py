from rest_framework import permissions, viewsets

from .models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Players to be viewed or edited.
    """
    queryset = Player.objects.all().order_by('-date_joined')
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
