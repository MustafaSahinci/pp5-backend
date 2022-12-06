from rest_framework import generics, permissions
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
    queryset = Car.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a car and edit or delete it if you own it.
    """
    serializer_class = CarSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Car.objects.all()