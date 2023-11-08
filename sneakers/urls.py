from django.urls import path, include
from sneakers.views import (SneakersListAPIView,
                            SneakersDetailAPIView,)


urlpatterns = [
    path('', SneakersListAPIView.as_view(), name='sneakers-main'),
    path('<str:pk>/', SneakersDetailAPIView.as_view(), name='sneakers-detail')
]

