"""team848 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from team848 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', views.ShowMovieFile.as_view(), name='showFile'),
    url(r'^admin/(?P<pk>\d+)/$', views.InAdminMovieDetail.as_view(), name='in_admin_movie_detail'), # /movie_input/movie/3


    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^movie_input/', include('movie_input.urls', namespace="movie_input")),
]

#url(r'^$', views.upload_file, name='upload_file'),
#    url(r'^home/$', views.home, name='home'),