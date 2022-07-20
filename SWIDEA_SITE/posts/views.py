from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    print(posts)

    context = {
        "posts":posts
    }
    return render(request, template_name="posts/home.html", context=context)

def create(request):
    if request.method == "POST":
        print(request.POST)
        idea = request.POST["idea"]
        req_photo = request.FILES["photo"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        tool = request.POST["tool"]

        Post.objects.create(idea = idea, photo = req_photo, content = content,
        interest = interest,tool = tool)

        return redirect("/")

    context = {}

    return render(request, template_name="posts/create.html",
    context = context)

def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        "post" : post,
    }
    return render(request, template_name="posts/detail.html",
    context = context)

def update(request, id):
    if request.method == "POST":
        idea = request.POST["idea"]
        req_photo = request.POST["photo"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        tool = request.POST["tool"]
    
        Post.objects.filter(id=id).update(idea=idea, photo=req_photo, content=content,
        interest=interest,tool=tool)

        return redirect(f"/post/{id}")

    elif request.method == "GET":
        post = Post.objects.get(id=id)
        context = {
            "post" : post
        }
        return render(request, template_name="posts/update.html",
        context=context)

def delete(request, id):
    if request.method =="POST":
        Post.objects.filter(id=id).delete()
        return redirect("/")

