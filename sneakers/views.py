from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


class SneakersListAPIView(APIView):
    def get(self, request: Request):
        return Response({'title': '123',})

    def post(self, request: Request):
        return Response({'t': 1,})

