from rest_framework.serializers import Serializer, ModelSerializer, DecimalField, CharField, UUIDField
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from sneakers.models import SneakersPair


# class SneakersPairSerializer(ModelSerializer):
#     class Meta:
#         model = SneakersPair
#         fields = "__all__"

#     def create(self, data):
#         return SneakersPair.objects.create(**data)

#     def delete(self):
#         return SneakersPair.objects.all().delete()

class SneakersSerializer(Serializer):
    id = UUIDField(read_only=True)
    src = CharField()
    title = CharField()
    price = DecimalField(10, 2)


class SneakersRetrieveCreateDestroySerializer(SneakersSerializer):
    # id = UUIDField(read_only=True)
    # src = CharField()
    # title = CharField()
    # price = DecimalField(10, 2)

    def create(self, data):
        return SneakersPair.objects.create(**data)


class SneakersDetailUpdateSerializer(SneakersSerializer):
    src = CharField(required=False)
    title = CharField(required=False)
    price = CharField(required=False)

    def update(self, instance: SneakersPair, validated_data: dict):
        instance.src = validated_data.get('src', instance.src)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    def delete(self, instance: SneakersPair):
        instance.delete()


