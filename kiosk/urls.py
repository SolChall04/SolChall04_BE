from django.urls import path
from . import views
from .views import menu_options


urlpatterns = [
    path('', views.landing),
    path('search_or_browse/', views.search_or_browse, name='search_or_browse'),
    path('search/', views.search, name='search'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:menu_id>/options/', menu_options, name='menu_options'),
]