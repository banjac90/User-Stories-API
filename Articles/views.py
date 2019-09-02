from rest_framework import generics
from rest_framework.permissions import *
from .models import *
from .serializers import *
from .permissions import *
from django.db.models import Q


class Category(generics.ListCreateAPIView):

	premission_classes = [IsAuthenticatedOrReadOnly,]
	serializer_class=CategorySerializer
	queryset = Category.objects.all()
	
		
class ArticleList(generics.ListAPIView):

	serializer_class = ArticleSerializer	
	premission_classes = [IsOwnerOrReadOnly,]

	def get_queryset(self):
		qs = Article.objects.all().order_by('-update_at')
		query = self.request.GET.get('q')
		if query is not None:
			qs = qs.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
		return qs

class ArticleCreate(generics.CreateAPIView):
	queryset = Article.objects.all()	
	serializer_class = ArticleSerializer
	premission_classes = [IsAuthenticated,]	
	

	def perform_create(self, serializer):
		serializer.save(created_by_user_id=self.request.user)

	
class ArticleDetailsEdit(generics.RetrieveUpdateAPIView):	
	queryset = Article.objects.all()	
	serializer_class = ArticleSerializer
	premission_classes = [IsOwnerOrReadOnly,]
	

class ArticleDelete(generics.RetrieveDestroyAPIView):	
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	premission_classes = [IsOwnerOrReadOnly,]
