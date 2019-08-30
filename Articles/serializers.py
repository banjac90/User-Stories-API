from .models import Category, Article
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = (
			'pk',			
			'title',
		)
		read_only_fields=['pk']


	def validate_title(self, value):
		"""Prevents Multiple titles for Categories"""
		queryset = Category.objects.filter(title__iexact=value)
		if self.instance:
			queryset = queryset.exclude(pk=self.instance.pk)
		if queryset.exists():
			raise serializers.ValidationError("This title has already been used")
		return value
		
	
class ArticleSerializer(serializers.ModelSerializer):
	created_by_user_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())
	
	class Meta:
		model = Article
		fields = (	
			'pk',		
			'category',
			'title',
			'created_by_user_id',			
			'update_at',
			'content',
			
		)
		read_only_fields = ['pk', 'update_at',]


		
	


