from rest_framework import serializers
from .models import Movie, Mpaa, Genre


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "name",
            "description",
            "img_path",
            "duration",
            "genre",
            "language",
            # "mpaa_id",
            "mpaa",
            "user_rating",
        ]

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'



class MpaaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mpaa
        fields = ["id", "mpaa_type", "mpaa_label"]

class MpaaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mpaa
        fields = '__all__'



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]

class GenreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'