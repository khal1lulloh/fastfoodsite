from django.urls import path
from .views import *

urlpatterns = [
	path('',ProductSerializersView.as_view()),
	path('api/<int:pk>/',ProductIDSerializersView.as_view()),
	path('registr/',AuthUserRegistrationView.as_view()),
	]