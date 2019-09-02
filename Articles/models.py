from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from rest_framework.reverse import reverse as api_reverse

class Category(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title

class Article(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	created_by_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	@property
	def owner(self):
		return self.created_by_user_id
