from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
	name=models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('theblog:add-post')

class Category_2(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('theblog:add-post')

class Post(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = RichTextField(blank = True, null=True)
	# body = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	post_date = models.DateField(auto_now_add=True)
	category_2 = models.CharField(max_length=255, default='coding')
	snippet = models.CharField(max_length=255, default='click to read more...')
	likes = models.ManyToManyField(User, related_name='blog_posts')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title + '|' + str(self.author)

	def get_absolute_url(self):
		return reverse('theblog:home')
