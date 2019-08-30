from django.urls import path
from .views import *

app_name = 'article-api'
urlpatterns = [
    
    path('ArticleList/', ArticleList.as_view(), name='Article-List'),   
    path('ArticleDelete/<int:pk>', ArticleDelete.as_view(), name='Article-Details'),
    path('ArticleCreate/', ArticleCreate.as_view(), name='Article-Create'),
    path('ArticleDetailsEdit/<int:pk>', ArticleDetailsEdit.as_view(), name='Article-Edit'),    
    path('Category/', Category.as_view(), name='Category-List-Create'),    

]