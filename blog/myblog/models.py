from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length=255)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')


class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) # associate the django User model and new one
	bio = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile')
	github_url = models.CharField(max_length=255, null=True, blank=True)
	twitter_url = models.CharField(max_length=255, null=True, blank=True)
	linkedin_url = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('home')


class Post(models.Model):
	title = models.CharField(max_length=255)
	header_image = models.ImageField(null=True, blank=True, upload_to='images/')
	# alternative for creating the tags using the db
	title_tag = models.CharField(max_length=255, default="My Blog")
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	# body = models.TextField()
	body = RichTextField(blank=True, null=True)
	post_date = models.DateField(auto_now_add=True)
	category = models.CharField(max_length=255, default="random")
	snippet = models.CharField(max_length=255, default="Click the link to read the post")
	likes = models.ManyToManyField(User, related_name='blog_posts') # related_name is like the ForeignKey

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		# where to redirect after creating new post
		# if redirects directly to the home page, the args are not neccessary
		# return reverse('article-detail', args=(str(self.id)) )
		return reverse('home')

	def total_likes(self):
		return self.likes.count()


