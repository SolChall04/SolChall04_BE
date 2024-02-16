from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu, Option
from django.db.models import Min
from django.http import JsonResponse
from .models import Store, Menu, Option, OptionContent, Cart, Order
from django.db.models import Sum


# Create your views here.
def landing(request):
    return render(request, 'kiosk/landing.html', {})

def search_or_browse(request):
    return render(request, 'kiosk/search_or_browse.html', {})

def search(request):
    return render(request, 'kiosk/search.html', {})

def menu(request):

    # Menu 모델에서 모든 메뉴를 가져옵니다.
    menus = Menu.objects.all()
    # Menu 모델에서 모든 고유한 카테고리를 가져옵니다.
    categories = Menu.objects.values_list('category', flat=True).distinct()

    # 가장 작은 menuId를 가지고 있는 카테고리를 가져옵니다.
    first_category = Menu.objects.order_by('menuId').first().category

    # menu.html 템플릿에 카테고리 목록과 메뉴 목록을 전달합니다.
    #return render(request, 'kiosk/menu.html', {'categories': categories, 'menus': menus})

    # 메뉴에 대한 옵션을 가져옵니다.


    return render(request, 'kiosk/menu.html',
                  {'categories': categories, 'menus': menus, 'first_category': first_category})

def cart(request):
    carts = Cart.objects.all()


    total_quantity = len(carts)
    total_price = Cart.objects.aggregate(total_price=Sum('price'))['total_price']

    return render(
    request,
    'kiosk/cart.html',
    {
        'carts': carts,
        'total_quantity': total_quantity,
        'total_price' : total_price
    }
)

def pay(request):

    return render(
    request,
    'kiosk/pay.html',
    {

    }
)

def success(request):
    latest_order = Order.objects.all().order_by('-pk').first()

    return render(
    request,
    'kiosk/order_success.html',
    {
        'latest_order' : latest_order
    }
)
