from django.urls import path
from .views import IndexPageViews,menuPageViews,AboutPageViews,BookPageViews,ProductCreateViews
from django.conf import settings
from django.conf.urls.static import static
from . import *


urlpatterns = [
	path('',IndexPageViews.as_view(),name='index'),
	path('menu/',views.menuPageViews,name='menu'),
	path('about/',AboutPageViews.as_view(),name='about'),
	path('book/',BookPageViews,name='book'),
	path('product_create/',ProductCreateViews.as_view(),name='product_create'),
	# path('products/<int:pk>/',productdetail, name=)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)