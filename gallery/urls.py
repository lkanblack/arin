from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_list, name='gallery_list'),
    path('gallery', views.gallery_detail, name='gallery_detail'),
    path('galereja', views.gallery_rus, name='gallery_rus'),
    path('hinnad', views.hind, name='hinnad'),
    path('rus', views.rus_page, name='rus'),
    path('remont', views.remont, name='remont'),
    path('shop', views.shop, name='shop'),
    path('paints', views.paint, name='paint'),
]