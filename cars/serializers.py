from rest_framework import serializers
from cars.models import Car
from saves.models import Save
from biddings.models import Bidding


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    save_id = serializers.SerializerMethodField()
    bidding_id = serializers.SerializerMethodField()
    saves_count = serializers.ReadOnlyField()
    biddings_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_save_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            save = Save.objects.filter(
                owner=user, car=obj
            ).first()
            return save.id if save else None
        return None

    def get_bidding_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            bidding = Bidding.objects.filter(
                owner=user, car=obj
            ).first()
            return bidding.id if bidding else None
        return None

    class Meta:
        model = Car
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'year', 'km', 'price', 'image',
            'image2', 'image3', 'image4', 'image_filter',
            'save_id', 'bidding_id', 'saves_count', 'biddings_count',
            'comments_count'
        ]
