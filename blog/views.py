from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

# Fonction pour la liste des posts
def post_list(request):
	
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	return render(request, 'blog/post_list.html', {'posts':posts})


def home(request):
	
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	return render(request, 'blog/home.html')

def apropos(request):
	
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	return render(request, 'blog/apropos.html')

def electronique(request):
	
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	return render(request, 'blog/electronique.html')

def informatique(request):
	
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	return render(request, 'blog/informatique.html')

def hybride(request):
	
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	return render(request, 'blog/hybride.html')

# Fonction pour le detail des focntion
def post_detail(request,pk):

	post = get_object_or_404(Post, pk=pk)
	posts = Post.objects.get(pk=pk)
	return render(request, 'blog/post_detail.html', {'post':posts})