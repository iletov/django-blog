from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy
# Create your views here.
# def home(request):
	# return render(request, 'home.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-post_date']
	# ordering = ['-id']


class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'


class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	# fields = '__all__' # for all the fields created in model class Post
	# fields = ('title', 'body')


class AddCategoryView(CreateView):
	model = Category
	# form_class = PostForm
	template_name = 'add_category.html'
	fields = '__all__'


class UpdatePostView(UpdateView):
	model = Post
	# form_class = UpdateForm
	template_name = 'update_post.html'
	fields = '__all__'


class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

# --------------------

def CategoryView(request, cat):
	category_posts = Post.objects.filter(category=cat)
	return render(request, 'categories.html', {'cat':cat.title(), 'category_posts':category_posts })