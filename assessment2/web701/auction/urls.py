from django.urls import path
from . import views

urlpatterns = [
    path('auction', views.auction, name='auction'),
    path('bid_item', views.bid_item, name='bid_item'),
    path('sell_item', views.sell_item, name='sell_item')
]