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
    path('menu/', views.menu),
    path('menu/add', views.add),


    # AJAX
    path('cart/del/', views.delete),
]