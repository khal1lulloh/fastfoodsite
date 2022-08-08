from django.urls import path
from .views import indexPageViews,menuPageViews,aboutPageViews,bookPageViews,ProductCreateViews
from django.conf import settings
from django.conf.urls.static import static
from . import *


urlpatterns = [
	path('',views.indexPageViews,name='index'),
	path('menu/',views.menuPageViews,name='menu'),
	# updateItem uchun
	path('update_item/',views.updateItem),
	# cart funsiyasi uchun 
	path('cart/', views.cart, name="cart"),
	path('about/',views.aboutPageViews,name='about'),
	path('book/',views.bookPageViews,name='book'),
	path('product_create/',ProductCreateViews.as_view(),name='product_create'),
	# path('products/<int:pk>/',productdetail, name=)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
