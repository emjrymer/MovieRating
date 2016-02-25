from django.contrib import admin

# Register your models here.
from app.models import Rater, Review, Movie

admin.site.register(Rater)
admin.site.register(Review)
admin.site.register(Movie)