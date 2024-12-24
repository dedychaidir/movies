from django.urls import path
from .views import Genres, GenreDetailView, MpaasView, MpaaDetailView, MoviesView
from .views import home_page_view, detail_page_view

urlpatterns = [
    path("", home_page_view, name="movie_list"),
    path("<int:pk>/", detail_page_view, name="movie_detail"),
    ### API's
    path("genres/", Genres.as_view()),
    path("genres/id/<int:pk>", GenreDetailView.as_view()),
    path("mpaas/", MpaasView.as_view()),
    path("mpaas/id/<int:pk>", MpaaDetailView.as_view()),
    path("movies/", MoviesView.as_view()),
]
