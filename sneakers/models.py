import uuid

from django.db.models import (ForeignKey,
                              CASCADE,
                              Model,
                              UUIDField,
                              CharField,
                              DecimalField,)


class SneakersPair(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    src = CharField(max_length=255)
    title = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)


class CartItem(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = ForeignKey(SneakersPair, on_delete=CASCADE, related_name='sneakers')

