from rest_framework import generics, permissions
from rest_framework.views import APIView
from .serializers import FollowerSerializer
from followers.models import Follower
from drf_api.permissions import IsOwnerOrReadOnly


class FollowerList(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FolowerDetail(generics.RetrieveDestroyAPIView):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classe = [IsOwnerOrReadOnly]
