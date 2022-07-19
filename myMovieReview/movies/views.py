from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def home(request):

    movies = Movie.objects.all()

    context = {
        "movies":movies
    }
    return render(request, template_name="movies/home.html", context=context)

def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        year = request.POST["year"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        time = request.POST["time"]
        review = request.POST["review"]

        Movie.objects.create(title = title, year = year, director = director,
        actor = actor, genre = genre, star = star, time = time,
        review = review)

        return redirect("/")

    context = {

    }

    return render(request, template_name="movies/create.html",
    context = context)

def detail(request, id):
    movie = Movie.objects.get(id=id)
    context = {
        "movie" : movie
    }
    return render(request, template_name="movies/detail.html",
    context = context)

def update(request,id):
    if request.method == "POST":
        title = request.POST["title"]
        year = request.POST["year"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        time = request.POST["time"]
        review = request.POST["review"]

        movie.save()
        
        Movie.objects.filter(id=id).update(title = title, year = year, director = director,
        actor = actor, genre = genre, star = star, time = time,
        review = review)

        
        return redirect(f"/movie/{id}")

    elif request.method == "GET":
        movie = Movie.objects.get(id=id)
        context = {
            "movie" : movie
        }    

        return render(request, template_name="movies/update.html",
        context=context)

def delete(request, id):
    if request.method =="GET":
        Movie.objects.filter(id=id).delete()
        return redirect("/")
