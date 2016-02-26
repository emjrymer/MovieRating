import operator
from django.shortcuts import render
from django.views.generic import View

from app.models import Movie, Review
from django.db.models import Avg


def index_view(request):
    return render(request, 'index.html', {})


def review_average(request):
    average_rating = []
    for item in Movie.objects.all():
        average_rating.append((item.movie_title, (Review.objects.filter(movie=item).aggregate(Avg('rating')))))
    movie_n_rating = []
    for item in average_rating:
        movie_n_rating.append((item[0], item[1]['rating__avg']))
    print(movie_n_rating)
    top_twenty = sorted(movie_n_rating, key=operator.itemgetter(1), reverse=True)[:20]
    return render(request, 'top_twenty.html', {'top20': top_twenty})


