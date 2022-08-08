from rest_framework import serializers
from my_app.models import Product
from accounts.models import User

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

	def create(self,validated_data):
		auth_user = User.objects.create_user(**validated_data)
		return auth_user