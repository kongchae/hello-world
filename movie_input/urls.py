from django.conf.urls import url
from movie_input import views

urlpatterns = [
    url(r'^$', views.MovieInputModelView.as_view(), name='index'), # /movie_input

    url(r'^movie/$', views.MovieList.as_view(), name='movie_list'), # /movie_input/movie/
    url(r'^movie/(?P<pk>\d+)/$', views.MovieDetail.as_view(), name='movie_detail'), # /movie_input/movie/3
]
