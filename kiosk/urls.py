from django.urls import path
from . import views


urlpatterns = [
    # path('cart/', views.OrderDetail.as_view()),
    path('cart/', views.cart),
    path('success/', views.success),
    path('pay/', views.pay, name='pay'),


    # AJAX
    path('cart/del/', views.delete),
]