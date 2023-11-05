from django.urls import path, include
from sneakers.views import SneakersListAPIView


urlpatterns = [
    path('', SneakersListAPIView.as_view(), name='sneakers-main'),
]

