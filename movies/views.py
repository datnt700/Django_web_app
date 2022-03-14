from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def create(request):
    if request.method == "POST":
        if request.POST.get('title') and request.POST.get('year') and request.POST.get('number') and request.POST.get('rate') and request.POST.get('genre'):
            savest = Movie()
            savest.title = request.POST.get('title')
            savest.release_year = request.POST.get('year')
            savest.number_in_stock = request.POST.get('number')
            savest.daily_rate = request.POST.get('rate')
            savest.genre = request.POST.get('genre')
            savest.save()
            messages.success(request, "The Record " +
                             savest.title + " Is Saved Successfully")
            return render(request, "movies/create.html")
    else:
        return render(request, "movies/create.html")


def detail(request, movie_id):
    try:
        movie = get_object_or_404(Movie, pk=movie_id)
        return render(request, 'movies/detail.html', {'movie': movie})
    except Movie.DoesNotExist:
        raise Http404
