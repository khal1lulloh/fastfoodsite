from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class AuthUserRegistrationView(APIView):
	permission_classes = (AllowAny)
	def post(self, request, *args, **kwargs):
		serializer = UserSerializer(data=request.data)
		for user in User.objects.all():
			if not user:
				break
			else:
				try:
					Token.objects.get(user_id=user.id)
				except TokenDoesNotExist:
					Token.objects.create(user=user)
		if serializer.is_valid():
			user = serializer.save()
			token = Token.objects.create(user=user)
			return Response(
				{
					"user":{
						"id":serializer.data["id"],
						"username":serializer.data["username"],
					},
					"status":{
						"message": "User created",
						"code": f"{status.HTTP_200_OK} OK",
					},
					"token": token.key,
				}
			)
		return Response(
			{
				"error": serializer.errors,
				"status": f"{status.HTTP_203_NON_AUTHORITATIVE_INFORMATION} NON AUTHORITATIVE INFORMATION"
			}
		)

class ProductSerializersView(ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class ProductIDSerializersView(RetrieveUpdateDestroyAPIView):
	permission_classes = [IsAuthenticated]
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
