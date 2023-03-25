from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('movie', MovieViewSet)
router.register('actor', ActorViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('movies/<int:pk>/actors', MovieActorAPIView.as_view(), name='actor-list'),
]