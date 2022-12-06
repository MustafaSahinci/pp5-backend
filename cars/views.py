from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from pp5.permissions import IsOwnerOrReadOnly
from .models import Car
from .serializers import CarSerializer


class CarList(generics.ListCreateAPIView):
    """
    List cars or create a car if logged in
    The perform_create method associates the car with the logged in user.
    """
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Car.objects.annotate(
        saves_count=Count('saves', distinct=True),
        # comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'saves__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'saves_count',
        # 'comments_count',
        'saves__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a car and edit or delete it if you own it.
    """
    serializer_class = CarSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Car.objects.annotate(
        saves_count=Count('saves', distinct=True),
        # comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')