from django.conf.urls import url, patterns
from api.views import MovieListView

urlpatterns = [
    url(r'^movies/', MovieListView.as_view(), name='movie_list'),
    # url(r'^genre/',GenreListView.as_view(), name='genre_list'),
    # url(r'^movies/(?P<pk>)$', MovieDetailView.as_view(), name='movie_detail'),
    # url(r'^users/', UserListView.as_view(), name='users'),
]
