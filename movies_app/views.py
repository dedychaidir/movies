from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Genre, Mpaa
from .serializers import (
    MovieSerializer,
    MovieDetailSerializer,
    MpaaSerializer,
    MpaaDetailSerializer,
    GenreSerializer,
    GenreDetailSerializer,
)


# Create your views here.
def home_page_view(request):
    # Retrieve all movies, or apply search filter if search term is provided
    search_query = request.GET.get("search", "")
    if search_query:
        movies = Movie.objects.filter(name__icontains=search_query)
    else:
        movies = Movie.objects.all()

    return render(
        request, "index.html", {"movies": movies, "search_query": search_query}
    )


def detail_page_view(request, pk):
    movie = get_object_or_404(Movie.objects.select_related().all(), pk=pk)
    print(movie)
    return render(request, "movie_detail.html", {"movie": movie})


class MoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the movie record to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailView(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        if not movie:
            return Response(
                {"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        if not movie:
            return Response(
                {"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = MovieDetailSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        if not movie:
            return Response(
                {"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
            )

        movie.delete()
        return Response(
            {"message": "Movie deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


########################################################################################
# GENRE
########################################################################################
class Genres(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the movie record to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetailView(APIView):
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        genre = self.get_object(pk)
        if not genre:
            return Response(
                {"error": "Genre not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = GenreSerializer(genre)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        genre = self.get_object(pk)
        if not genre:
            return Response(
                {"error": "Genre not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = GenreDetailSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        genre = self.get_object(pk)
        if not genre:
            return Response(
                {"error": "Genre not found"}, status=status.HTTP_404_NOT_FOUND
            )

        genre.delete()
        return Response(
            {"message": "Genre deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


########################################################################################
# MPAA
########################################################################################
class MpaasView(APIView):
    def get(self, request):
        mpaas = Mpaa.objects.all()
        serializer = MpaaSerializer(mpaas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MpaaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the movie record to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MpaaDetailView(APIView):
    def get_object(self, pk):
        try:
            return Mpaa.objects.get(pk=pk)
        except Mpaa.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        mpaa = self.get_object(pk)
        if not mpaa:
            return Response(
                {"error": "Mpaa not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = MpaaSerializer(mpaa)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        mpaa = self.get_object(pk)
        if not mpaa:
            return Response(
                {"error": "Mpaa not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = MpaaDetailSerializer(mpaa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        mpaa = self.get_object(pk)
        if not mpaa:
            return Response(
                {"error": "Mpaa not found"}, status=status.HTTP_404_NOT_FOUND
            )

        mpaa.delete()
        return Response(
            {"message": "Mpaa deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
