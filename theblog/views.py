from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Category, Post, Category_2
from .forms import PostForm
from django.urls import reverse_lazy



class CategoryCreateView(CreateView):
	model = Category
	# form_class = PostForm
	template_name = 'theblog/ad_category.html'
	fields = '__all__'


def CategoryView(request, cats):
	category_posts = Post.objects.filter(category_2=cats)
	cat_menu = Category_2.objects.all()
	return render(request,'theblog/category.html', {'cats':cats,'category_posts':category_posts,'cat_menu':cat_menu})

class PostListView(ListView):
	model = Post
	template_name = 'theblog/home.html'
	ordering = ['-post_date']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category_2.objects.all()
		context = super(PostListView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class PostDetailView(DetailView):
	model = Post
	template_name = 'theblog/post_detail.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category_2.objects.all()
		context = super(PostDetailView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context	

class Category2CreateView(CreateView):
	model = Category_2
	# form_class = PostForm
	template_name = 'theblog/add_category2.html'
	fields = '__all__'

class PostCreateView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'theblog/add_post.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category_2.objects.all()
		context = super(PostCreateView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context	



class PostUpdateView(UpdateView):
	model = Post
	# form_class = UpdateForm
	template_name = 'theblog/update_post.html'
	fields = ['category','title','body']

class PostDeleteView(DeleteView):
	model = Post
	# form_class = UpdateForm
	template_name = 'theblog/delete_post.html'
	success_url = reverse_lazy('theblog:home')
	# success_url = reverse_lazy('theblog:home')
# def detail(request, post_id):
# 	try:
# 		post = Post.objects.get(pk=post_id)
# 	except Post.DoesNotExist:
# 		raise Http404('Post does not exist')
# 	return render(request, 'theblog/post_detail.html', {'post':post})



