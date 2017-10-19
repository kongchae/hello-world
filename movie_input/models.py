from django.db import models


class MovieManager(models.Manager):
    def create_movie(self, title, movie_path):
        movie = self.create(title=title, movie_path=movie_path)
        # do something with the book
        return movie


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True)
    movie_path = models.FileField(upload_to='uploads/', null=True)

    def __unicode__(self):
        return self.title

    objects = MovieManager()


# movie = Movie.objects.create_movie("Pride and Prejudice")
