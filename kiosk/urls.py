from django.urls import path
from . import views


urlpatterns = [
    # path('cart/', views.OrderDetail.as_view()),
    path('cart/', views.cart, name='cart'),
    path('success/', views.success),
    path('pay/', views.pay, name='pay'),


    # test
    path('login/', views.login),
    path('signup/', views.signup),
    path('menu/', views.admin_menu),
    path('menu/add', views.add),


    # AJAX
    path('cart/del/', views.delete),


    
    path('', views.landing),
    path('search_or_browse/', views.search_or_browse, name='search_or_browse'),
    path('search/', views.search, name='search'),
    path('browse/', views.browse, name='browse'),
    #path('menu/<int:menu_id>/options/', menu_options, name='menu_options'),
    #path('menu/<int:menu_id>/options/', views.menu_options, name='menu_options'),
    path('menu/<int:menu_id>/', views.menu_options, name='menu_detail'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
]