from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.serializers import ModelSerializer
from rest_framework import generics
from rest_framework import viewsets

from sneakers.models import SneakersPair
from sneakers.serializers import SneakersSerializer


class SneakersViewSet(viewsets.ModelViewSet):
    queryset = SneakersPair.objects.all()
    serializer_class = SneakersSerializer

    def destroy(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(instance)
        super().destroy(request, *args, **kwargs)
        return Response({'instance': serializer.data})

