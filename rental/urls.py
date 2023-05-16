from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings 
from . import views

urlpatterns = [
    path('notice/',views.notice,name="notice"),
    path('store/',views.store,name="store"),
    path('home/',views.home,name="home"),
    path('logout/',views.logout,name="logout"),
    path('<int:id>/', views.detail_view, name='detail'),
    path('',views.blog_view,name="blog"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
 