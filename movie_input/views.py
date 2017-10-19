from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from movie_input.models import Movie
''' 파일업로드 관련'''
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


#--- TemplateView
class MovieInputModelView(TemplateView):

    template_name = 'movie_input/index.html'

    def get_context_data(self, **kwargs):
        context = super(MovieInputModelView, self).get_context_data(**kwargs)
        context['object_list'] = ['Movie']
        return context


#--- ListView
class MovieList(ListView):
    model = Movie


#--- DetailView
class MovieDetail(DetailView):
    model = Movie


''' 잠시 쓴 것임'''
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'movie_input/../../../templates/upload.html', {'form': form})


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

