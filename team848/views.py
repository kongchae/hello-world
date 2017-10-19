from django.views.generic import DetailView
from django.views.generic.base import TemplateView


#--- TemplateView
from movie_input.models import Movie


class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['object_list'] = ['movie_input']
        return context


class ShowMovieFile(TemplateView):

    template_name = 'uploaded.html'

    def get_context_data(self, **kwargs):
        context = super(ShowMovieFile, self).get_context_data(**kwargs)

        return context


class InAdminMovieDetail(TemplateView):

    template_name = 'uploaded.html'

    def get_context_data(self, **kwargs):
        context = super(InAdminMovieDetail, self).get_context_data(**kwargs)

        return context


class InAdminMovieDetail(DetailView):
        model = Movie