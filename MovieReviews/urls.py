"""MovieReviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app.views import top_twenty, on_click, rater_on_click, index_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name='index_view'),
    url(r'^TopTwenty', top_twenty, name="TopTwenty"),
    url(r'^(?P<pk>\d+)$', on_click, name="one_movie_view"),
    url(r'^rater(?P<pk>\d+)$', rater_on_click, name="one_rater_view")

]
