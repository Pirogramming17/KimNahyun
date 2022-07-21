from django.shortcuts import render, redirect
from .models import Post, Tool

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

def toolhome(request):
    tools = Tool.objects.all()
    context = {
        "tools": tools
    }
    return render(request, template_name='posts/toolhome.html', context=context)

def toolcreate(request):
    if request.method == "POST":
        name = request.POST["name"]
        kind = request.POST["kind"]
        content = request.POST["content"]

        Tool.objects.create(
        name=name,
        kind=kind,
        content=content
        )
    return render(request, template_name='posts/toolcreate.html')

def tooldetail(request, id):
    tool = Tool.objects.get(id=id)
    context = {
        "tool": tool,
        "ideas": Post.objects.filter(tool=tool)
    }
    return render(request, template_name="posts/tooldetail.html", context=context)

def toolupdate(request, id):
    tool = Tool.objects.get(id=id)
    if request.method == "POST":
        name = request.POST["name"]
        kind = request.POST["kind"]
        content = request.POST["content"]

        Tool.objects.filter(id=id).update(
        name = name,
        kind = kind,
        content = content,
        )
        return redirect(f"/tooldetail/{id}")

    elif request.method == "GET":
        tool = Tool.objects.get(id=id)
        context = {
        "tool": tool
        }
    return render(request, 'posts/toolupdate.html', context=context)

def tooldelete(request, id):
    if request.method == "POST":
        Tool.objects.filter(id=id).delete()
        return redirect('/')

