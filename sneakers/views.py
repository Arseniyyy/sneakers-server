from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError

from sneakers.models import SneakersPair
from sneakers.serializers import (SneakersRetrieveCreateDestroySerializer,
                                  SneakersDetailUpdateSerializer,)


class SneakersListAPIView(APIView):
    def get(self, request: Request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        return Response({'queryset': serializer.data})

    def post(self, request: Request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer=serializer)
        return Response({
            'instance': serializer.data
        })

    def delete(self, request: Request):
        model = self.get_model()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(model.objects.all(), many=True)
        serializer.delete()
        return Response({
            'instances': serializer.data
        })

    def get_queryset(self) -> list[SneakersPair]:
        return SneakersPair.objects.all()

    def perform_create(self, serializer: ModelSerializer) -> SneakersPair:
        serializer.save()

    def get_serializer_class(self):
        return SneakersRetrieveCreateDestroySerializer

    def get_model(self):
        return SneakersPair


class SneakersDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        primary_key = kwargs.get('pk')
        model = self.get_model()

        try:
            instance = model.objects.get(pk=primary_key)
        except model.DoesNotExist:
            return Response({'error': 'Object does not exist.'})
        except ValidationError:
            return Response({'error': 'The provided id is not a valid UUID.'})

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(instance=instance)
        return Response({'instance': serializer.data})

    def delete(self, request: Request, *args, **kwargs):
        primary_key = kwargs.get('pk')
        self.check_if_not_primary_key(primary_key, raise_exception=True)
        instance = self.get_object(primary_key)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(instance=instance)
        self.perform_destroy(instance=instance, serializer=serializer)

        return Response({'instance': {**serializer.data, 'id': primary_key}})

    def patch(self, request: Request, *args, **kwargs):
        primary_key = kwargs.get('pk', None)
        payload = request.data
        if not primary_key:
            return Response({'error': 'No primary key provided'})
        if not payload:
            return Response({'error': 'No data provided'})

        try:
            instance = self.get_model().objects.get(pk=primary_key)
        except:
            return Response({'error': 'Object not found'})

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(instance=instance, data=payload)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'instance': serializer.data})

    def get_queryset(self):
        return SneakersPair.objects.all().values()

    def get_serializer_class(self):
        return SneakersDetailUpdateSerializer

    def get_model(self):
        return SneakersPair

    def get_object(self, primary_key: str):
        return self.get_model().objects.get(pk=primary_key)

    def perform_destroy(self, instance: SneakersPair, serializer: SneakersDetailUpdateSerializer):
        serializer.delete(instance)

    def check_if_not_primary_key(self, primary_key: str, raise_exception: bool):
        if not primary_key:
            if raise_exception:
                return Response({'error': 'No primary key provided'})
            return True
        return False

