from django import forms
from .models import Movie


class UploadFileForm(forms.Form):
    class Meta:
        model = Movie
        fields = ('title', 'movie_path')



'''
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'movie_path')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False
'''
