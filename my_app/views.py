from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import Product,Comment,Order
from django.core.paginator import Paginator
import requests
from django.urls import reverse_lazy
# Create your views here.

class IndexPageViews(ListView):
	model = Product
	template_name = 'index.html'

def menuPageViews(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total': 0, "get_cart_items": 0}
		cartItems = order['get_cart_items']

	obj = Product.objects.all()
	page_n = request.GET.get('page',1)
	p = Paginator(obj,3)
	try:
		page = p.page(page_n)
	except Exception:
		page = p.page(1)
	context = {
	'page': page,
	'cartItems': cartItems
	}
	return render(request,'menu.html',context)

class AboutPageViews(TemplateView):
	template_name = 'about.html'

class ProductCreateViews(CreateView):
	model = Product
	# fields = ('product_name','product_description','product_image','product_price')
	fields='__all__'
	success_url = reverse_lazy('index')
	template_name = 'product_create.html'

# class BookPageViews(TemplateView):
# 	template_name = 'book.html'

def telegram_bot_sendtext(bot_message):
    bot_token = '5269225627:AAFwEXlOuhI3ArUY2YPXyEd-VP5rUThcKXE'
    bot_chatID = '692799479'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)   
    return response.json()

def BookPageViews(request):
    if request.method == 'POST':
        name = request.POST.get('name',None)
        phone = request.POST.get('phone',None)
        email = request.POST.get('email',None)
        message = request.POST.get('message',None)
        user = Comment.objects.create(
            userName = name,
            phone = phone,
            email = email,
            message = message
            )
        user.save()
        telegram_bot_sendtext(f"{user}\nTelefon raqami: {phone}\nXabari: {message}")
        
       
    return render(request=request,template_name= 'book.html')

