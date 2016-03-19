from django.shortcuts import render
from django.utils import timezone
from .models import Post,Biographie
from django.shortcuts import render, get_object_or_404
from .forms import PostForm,ContactForm
from django.shortcuts import redirect

# Create your views here.

# Fonction pour la liste des posts
def post_list(request):
	
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	return render(request, 'blog/post_list.html', {'posts':posts})


def home(request):
	
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	return render(request, 'blog/home.html')

def apropos(request):
	
	
	bio = Biographie.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = form.save(commit=True)
			contact.created_date = timezone.now()
			contact.save()
	else:
		form = ContactForm()
	return render(request, 'blog/apropos.html',{'biographie':bio,'form':form})

def electronique(request):
	
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	return render(request, 'blog/electronique.html', {'posts':posts})

def informatique(request):
	
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	return render(request, 'blog/informatique.html', {'posts':posts})

def hybride(request):
	
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	return render(request, 'blog/hybride.html', {'posts':posts})

# Fonction pour le detail des focntion
def post_detail(request,pk):

	post = get_object_or_404(Post, pk=pk)
	posts = Post.objects.get(pk=pk)
	return render(request, 'blog/post_detail.html', {'post':posts})

#Fonction pour le formulaire
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})
