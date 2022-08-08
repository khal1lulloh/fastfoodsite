from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
# class UserCreateView(generic.CreateView):
# 	form_class = UserCreationForm
# 	success_url = reverse_lazy('login')
# 	template_name = 'signup.html'

def register_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = User.objects.create_user(username=username,password=password)
		user.save()
		return redirect('login')

	ctx ={}
	return render(request,'signup.html',ctx)

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username,password = password)
		print("USER",user)
		if user:
			login(request,user)
			return redirect('index')

	ctx ={}
	return render(request,'registration/login.html',ctx)

def logout_user(request):
	logout(request)
	return redirect('index')
