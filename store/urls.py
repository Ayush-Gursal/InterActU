from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('logout/',views.logout,name="logout"),
    path('rental/',views.rental,name="rental"),
    path('notice/',views.notice,name="notice"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('', views.store, name="store"),
    
]