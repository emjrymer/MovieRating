import operator
from django.shortcuts import render, get_list_or_404
from django.views.generic import View

from app.models import Movie, Review
from django.db.models import Avg


def index_view(request):

    return render(request, 'index.html', {})


#def one_movie_view(request):
   # return render(render, 'one_movie.html', {})


#don't use
'''def review_average(request):
    average_rating = []
    for item in Movie.objects.all():
        average_rating.append((item.movie_title, (Review.objects.filter(movie=item).aggregate(Avg('rating')))))
    movie_n_rating = []
    for item in average_rating:
        movie_n_rating.append((item[0], item[1]['rating__avg']))
    top_twenty = sorted(movie_n_rating, key=operator.itemgetter(1), reverse=True)[:20]
    return render(request, 'top_twenty.html', {'top20': top_twenty})'''


def top_twenty(request):
    movie_avg_rating = []
    for item in Movie.objects.all():
        movie_avg_rating.append((item.movie_title, item.avg_rating))
    top_sorted = sorted(movie_avg_rating, key=lambda x: x[1], reverse=True)[:20]
    return render(request, 'top_twenty.html', {'top20': top_sorted})


def every_movie_view(request):
    average_rating = []
    for item in Movie.objects.all():
        average_rating.append((item.movie_title, (Review.objects.filter(movie=item).aggregate(Avg('rating')))))
    movie_rating = []
    for item in average_rating:
        movie_rating.append((item[0], item[1]['rating__avg']))
    all_movies = sorted(movie_rating, key=lambda x: x[1], reverse=True)
    return render(request, 'index.html', {'all_movies': all_movies})


#don't need this
'''def get_reviewer_and_movie(request):
    individual_people_movie = []
    for item in Review.objects.all():
        individual_people_movie.append((item.reviewer.id, item.movie))
    print(individual_people_movie)
    return render(request, 'index.html', {'all_review': individual_people_movie})'''

