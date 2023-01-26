from rest_framework import serializers
from .models import Bidding


class BiddingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Bidding model
    Adds three extra fields when returning a list of bidding instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Bidding
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'car', 'created_at', 'updated_at', 'content'
        ]


class BiddingDetailSerializer(BiddingSerializer):
    """
    Serializer for the Bidding model used in Detail view
    car is a read only field so that we dont have to set it on each update
    """
    car = serializers.ReadOnlyField(source='car.id')
