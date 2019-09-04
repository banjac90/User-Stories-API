from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_swagger.views import get_swagger_view
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


urlpatterns = [
	

    path('admin/', admin.site.urls),
    path('article-api/', include('Articles.urls', namespace='articles-api')),
    path('Users/', include('Users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls')),

    #login with jwt token, refresh token and verify token
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenRefreshView.as_view()),
    
    path('openapi', get_schema_view(
        title="User Stories API",
        description="API for User Stories"        
    ), name='openapi-schema'),


    path('swagger-ui/',TemplateView.as_view(
    	template_name='swagger-ui.html',
    	extra_context = {'schema_url':'openapi-schema'}
    	), name='swagger-ui')

]
