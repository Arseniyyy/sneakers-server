from rest_framework.serializers import (Serializer,
                                        ModelSerializer,
                                        DecimalField,
                                        CharField,
                                        UUIDField,)

from sneakers.models import SneakersPair


class SneakersSerializer(ModelSerializer):
    class Meta:
        model = SneakersPair
        fields = "__all__"

    def create(self, data):
        return SneakersPair.objects.create(**data)

