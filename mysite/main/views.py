from django.shortcuts import render
from .models import Post

def index(request):
    postAll = Post.objects.all()
    return render(request, 'main/index.html', {"postAll" : postAll})
# Create your views here.
