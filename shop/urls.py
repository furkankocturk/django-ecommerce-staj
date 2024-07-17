from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
]
urlpatterns = [
    path("", views.home, name='home'),
    path("", views.home, name='link'),
    path("", views.home, name='Action'),
    path("", views.home, name='Another action'),
    path("", views.home, name='something else here'),
    path("categories", views.categories, name='something else'),
    path("kategoriler", views.categories, name='something else'),
    path('category/<str:category_name>/', views.category_detail, name='category_detail'),
    path('store/<str:store_name>/', views.store_detail, name='store_detail'),






path("", views.home, name='disable'),
path("", views.home, name='favorilerim'),
path("", views.home, name='sepetim'),
]