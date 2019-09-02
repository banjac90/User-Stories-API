from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import password_validation as validators
from rest_framework import exceptions
from rest_auth.serializers import LoginSerializer 

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	
	class Meta(object):
		model = User
		fields = ('id', 'email', 'first_name', 'last_name', 'password')
		
	#validate password		
	def validate(self, data):
		user = User(**data)
		password = data.get('password')

		errors = dict()
		try:
			validators.validate_password(password=password, user=User)
		except exceptions.ValidationError as e:
			errors['password'] = list(e.messages)

		if errors:
			raise serializers.ValidationError(errors)
		return super(UserSerializer, self).validate(data)	

	def create(self, validated_data):
		return User.objects.create_user(**validated_data)
 
class UserDetailsSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('email', 'password')


# Get the UserModel
UserModel = User

class UserLoginSerializer(LoginSerializer):   
	username = None
	email = serializers.EmailField(required=True)
