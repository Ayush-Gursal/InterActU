from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings 
from . import views

urlpatterns = [
    path('store/',views.store,name="store"),
    path('home/',views.home,name="home"),
    path('logout/',views.logout,name="logout"),
    path('rental/',views.rental,name="rental"),
    path('',views.notice,name="notice"),
]
