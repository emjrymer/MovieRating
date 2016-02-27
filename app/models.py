from django.db import models

# Create your models here.


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=2)
    occupation = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)


class Movie(models.Model):
    movie_title = models.CharField(max_length=30)
    release_date = models.CharField(max_length=30)
    video_release_date = models.CharField(max_length=30, blank=True, default="")
    imdb = models.URLField()
    unknown_genre = models.BooleanField(default=0)
    action = models.BooleanField(default=0)
    adventure = models.BooleanField(default=0)
    animation = models.BooleanField(default=0)
    childrens = models.BooleanField(default=0)
    comedy = models.BooleanField(default=0)
    crime = models.BooleanField(default=0)
    documentary = models.BooleanField(default=0)
    drama = models.BooleanField(default=0)
    fantasy = models.BooleanField(default=0)
    filmnoir = models.BooleanField(default=0)
    horror = models.BooleanField(default=0)
    musical = models.BooleanField(default=0)
    mystery = models.BooleanField(default=0)
    romance = models.BooleanField(default=0)
    scifi = models.BooleanField(default=0)
    thriller = models.BooleanField(default=0)
    war = models.BooleanField(default=0)
    western = models.BooleanField(default=0)
    avg_rating = models.FloatField(null=True)

    def __str__(self):
        return self.movie_title


class Review(models.Model):
    reviewer = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()

    def __str__(self):
        return self.movie.movie_title
