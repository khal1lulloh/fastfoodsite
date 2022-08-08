from django.urls import path
from .views import MahsulotlarSerializersView, MahsulotlarIDSerializersView

urlpatterns = [
	path('',MahsulotlarSerializersView.as_view()),
	path('<int:pk>/',MahsulotlarIDSerializersView.as_view()),
	]