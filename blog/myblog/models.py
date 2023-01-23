from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
	title = models.CharField(max_length=255)
	# alternatie for creating the tags using the db
	title_tag = models.CharField(max_length=255, default="My Blog")
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	post_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		# where to redirect after creating new post
		# if redirects directly to the home page, the args are not neccessary
		# return reverse('article-detail', args=(str(self.id)) )
		return reverse('home')


