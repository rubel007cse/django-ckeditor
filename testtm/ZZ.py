from django.shortcuts import get_object_or_404
from coolapp.models import Post
from django.shortcuts import render, redirect


def index(request, postid=None):

    post = get_object_or_404(Post, id=postid)

    if request.method == "POST":
        id = request.POST['postid']
        content = request.POST['content']
        print('data', id, content)
        return '/'

    return render(request, 'post.html', {
        'my_objects': post
    })