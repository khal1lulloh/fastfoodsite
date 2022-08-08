from rest_framework import serializers
from .models import Mahsulotlar

class MahsulotlarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mahsulotlar
		fields = '__all__'