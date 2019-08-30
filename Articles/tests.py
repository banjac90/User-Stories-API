from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Article, Category

User = get_user_model()

class ArticleTestCase(APITestCase):
	def setUp(self):
		user_obj = User(email='test@testmail.com', first_name='Test', last_name='User')
		user_obj.set_password("Strongpass!1")
		user_obj.save()
		category = Category.objects.get(id=1)
		article = Article.objects.create(
			category=category, 
			created_by_user_id=user_obj, 
			title='testtitle', 
			content='test content'
			)

	def test_single_user(self):
		user_count = User.objects.count()
		self.assertEqual(user_count, 1)

	def test_single_article(self):
		article_count = Article.objects.count()
		self.assertEqual(article_count, 1)