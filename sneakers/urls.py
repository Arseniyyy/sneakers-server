from django.urls import path, include
from rest_framework import routers

from sneakers.views import SneakersViewSet


router = routers.SimpleRouter()
router.register(r's', SneakersViewSet)

urlpatterns = [
    path('', include(router.urls))
]

