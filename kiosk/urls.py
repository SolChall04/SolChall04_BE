from django.urls import path
from . import views


urlpatterns = [
    # path('cart/', views.OrderDetail.as_view()),
    path('cart/', views.cart),
    path('success/', views.success),
    path('pay/', views.pay, name='pay'),
    path('', views.landing),
    path('search_or_browse/', views.search_or_browse, name='search_or_browse'),
    path('search/', views.search, name='search'),
    path('menu/', views.menu, name='menu'),
    #path('menu/<int:menu_id>/options/', menu_options, name='menu_options'),
    #path('menu/<int:menu_id>/options/', views.menu_options, name='menu_options'),
    path('menu/<int:menu_id>/', views.menu_options, name='menu_detail'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
]