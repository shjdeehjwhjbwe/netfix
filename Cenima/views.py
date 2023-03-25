from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .serializers import MovieSerializer, ActorSerializer
from .models.movie import Movie
from .models.actor import Actor


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    @action(detail=True, methods=['POST'])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor = Actor.objects.get(id=request.data.get("id"))
        movie.actors.add(actor)
        serializer = ActorSerializer(movie.actors.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['DELETE'])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor = Actor.objects.get(id=request.data.get("id"))
        movie.actors.remove(actor)
        serializer = ActorSerializer(movie.actors.all(), many=True)
        return Response(serializer.data)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = LimitOffsetPagination


class MovieActorAPIView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        serializer = ActorSerializer(movie.actors.all(), many=True)
        return Response(serializer.data)