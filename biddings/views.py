from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from pp5.permissions import IsOwnerOrReadOnly
from .models import Bidding
from .serializers import BiddingSerializer, BiddingDetailSerializer


class BiddingList(generics.ListCreateAPIView):
    """
    List bidding or create a bidding if logged in.
    """
    serializer_class = BiddingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Bidding.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['car']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BiddingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a bidding, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BiddingDetailSerializer
    queryset = Bidding.objects.all()
