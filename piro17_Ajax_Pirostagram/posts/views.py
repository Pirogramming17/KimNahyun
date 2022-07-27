from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def main(request):
    comments = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else :
            return redirect('/')
    else :
        form = CommentForm()
        context={
            'form':form,
            'comments':comments,
        }
        return render(request, 'posts/main.html', context=context)

@csrf_exempt
def like(request):
    req = json.loads(request.body)
    comment_id = req['id']
    comment = Comment.objects.get(id=comment_id)
    if comment.like == True:
        comment.like = False
    elif comment.like == False:
        comment.like = True
    comment.save()
    return JsonResponse({'id':comment_id, 'type' : comment.like})

@csrf_exempt
def delete(request):
    req = json.loads(request.body)
    comment_id = req['id']
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return JsonResponse({'id' : comment_id})