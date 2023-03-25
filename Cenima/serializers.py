from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from datetime import date
from .models.movie import Movie
from .models.actor import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'first_name', 'brithdate', 'gender')

    def validate_birthdate(self, value):
        if value <= date(1950, 1, 1):
            raise ValidationError(detail='Not allowed year. Min 1951')
        return value


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    class Meta:
        model = Movie
        fields =       ('id', 'name', 'year', 'genre', 'imdb', 'actors')
