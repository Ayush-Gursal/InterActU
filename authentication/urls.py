from django.urls import path

from . import views

urlpatterns = [
   
    
    path('logout/',views.logoutUser,name="logout"),
    path('rental/',views.rental,name="rental"),
    path('store/',views.store,name="store"),
    path('home/',views.home,name="home"),
    path('register/',views.registerPage,name="register"),
    
    path('',views.loginPage,name="login"),
]
