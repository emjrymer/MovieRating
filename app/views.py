import operator
from django.shortcuts import render, get_list_or_404
from django.views.generic import View

from app.models import Movie, Review, Rater
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
    return render(request, 'top_twenty.html', {'top20': top_twenty})


def top_twenty(request):
    movie_avg_rating = []
    for item in Movie.objects.all():
        movie_avg_rating.append((item.movie_title, item.avg_rating))
    top_sorted = sorted(movie_avg_rating, key=lambda x: x[1], reverse=True)[:20]
    return render(request, 'top_twenty.html', {'top20': top_sorted})'''


def top_twenty(request):
    top = Movie.objects.order_by('-avg_rating')[:20]
    return render(request, 'top_twenty.html', {'top20': top})


def on_click(request, pk):
    reviewers = get_list_or_404(Review, movie_id=pk)
    movie = Movie.objects.get(id=pk)
    return render(request, 'one_movie.html', {'reviewers': reviewers, 'movie': movie})


'''def every_rater_view(request):
    all_raters = Rater.objects.all()
    return render(request, 'one_rater_view.html', {'all_raters': all_raters})'''


def rater_on_click(request, pk):
    x = Rater.objects.get(id=pk)
    movies = Review.objects.filter(reviewer=x.pk)
    #all movies that match the raters id?
    return render(request, 'one_rater_view.html', {'raters': x, 'movies': movies})


def every_movie_view(request):
    all_movies = Movie.objects.all()
    return render(request, 'index.html', {'all_movies': all_movies})

#don't need this
'''def every_movie_view(request):
    average_rating = []
    for item in Movie.objects.all():
        average_rating.append((item.movie_title, (Review.objects.filter(movie=item).aggregate(Avg('rating')))))
    movie_rating = []
    for item in average_rating:
        movie_rating.append((item[0], item[1]['rating__avg']))
    all_movies = sorted(movie_rating, key=lambda x: x[1], reverse=True)
    return render(request, 'index.html', {'all_movies': all_movies})



def get_reviewer_and_movie(request):
    individual_people_movie = []
    for item in Review.objects.all():
        individual_people_movie.append((item.reviewer.id, item.movie))
    print(individual_people_movie)
    return render(request, 'index.html', {'all_review': individual_people_movie})'''

