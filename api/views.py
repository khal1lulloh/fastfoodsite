from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

class MahsulotlarSerializersView(ListAPIView):
	queryset = Mahsulotlar.objects.all()
	serializer_class = MahsulotlarSerializer

class MahsulotlarIDSerializersView(RetrieveAPIView):
	permission_classes = [IsAuthenticated]
	queryset = Mahsulotlar.objects.all()
	serializer_class = MahsulotlarSerializer
