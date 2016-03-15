import json
import operator

from django.core.urlresolvers import reverse
from django.forms import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_list_or_404
from django.views.generic import View

from app.models import Movie, Review, Rater, Ureview
from django.db.models import Avg


def index_view(request):
    all_movies = Movie.objects.all()
    user_review = request.POST.get('review_movie')
    movie_review = request.POST.get('message_body')
    if user_review and movie_review:
        Ureview.objects.create(user_review=user_review, movie_review=movie_review)
        return HttpResponseRedirect(reverse('app.views.index_view'))
    all_ureview = Ureview.objects.all()
    return render(request, "index.html", {"all_ureview": all_ureview, 'all_movies': all_movies})


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


#don't need this
'''
def every_movie_view(request):
    all_movies = Movie.objects.all()
    return render(request, 'index.html', {'all_movies': all_movies})

#don't need this
def every_movie_view(request):
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


class FullMovieListApiView(View):

    def get(self, request):
        movie_list = list(Movie.objects.all().values())
        return HttpResponse(json.dumps(movie_list), content_type='application/json')

    def post(self, request):
        movie_title = request.POST.get('movie_title')
        release_date = request.POST.get('release_date')
        video_release_date = request.POST.get('video_release_date')
        imdb = request.POST.get('imdb')
        movie_object = Movie.objects.create(movie_title=movie_title, release_date=release_date, video_release_date=video_release_date, imdb=imdb)
        movie_dict = model_to_dict(movie_object)
        return HttpResponse(json.dumps(movie_dict), status=201, content_type='application/json')


class FullRaterListApiView(View):

    def get(self, request):
        rater_list = list(Rater.objects.all().values())
        return HttpResponse(json.dumps(rater_list), content_type='application/json')

    def post(self, request):
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        occupation = request.POST.get('occupation')
        zip_code = request.POST.get('zip_code')
        rater_object = Rater.objects.create(age=age, gender=gender, occupation=occupation, zip_code=zip_code)
        rater_dict = model_to_dict(rater_object)
        return HttpResponse(json.dumps(rater_dict), status=201, content_type='application/json')


class FullReviewListApiView(View):

    def get(self, request):
        review_list = list(Review.objects.all().values())
        return HttpResponse(json.dumps(review_list), content_type='application/json')

    def post(self, request):
        reviewer_id = request.POST.get('reviewer_id')
        movie_id = request.POST.get('movie_id')
        rating = request.POST.get('rating')
        review_object = Review.objects.create(reviewer_id=reviewer_id, movie_id=movie_id, rating=rating)
        review_dict = model_to_dict(review_object)
        return HttpResponse(json.dumps(review_dict), status=201, content_type='application/json')


class SingleMovieApiView(View):

    def get(self, request, pk):
        movie = list(Review.objects.filter(id=pk).values())
        return HttpResponse(json.dumps(movie), content_type='application/json')


class SingleRaterApiView(View):

    def get(self, request, pk):
        rater = list(Review.objects.filter(id=pk).values())
        return HttpResponse(json.dumps(rater), content_type='application/json')


class SingleReviewApiView(View):

    def get(self, request, pk):
        review = list(Review.objects.filter(id=pk).values())
        return HttpResponse(json.dumps(review), content_type='application/json')

