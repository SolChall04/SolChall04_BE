from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu, Option
from django.db.models import Min
from django.http import JsonResponse

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


# def menu_options(request, menu_id):
#     menu = Menu.objects.get(pk=menu_id)
#     #menu = Menu.objects.get(menuId=1)
#     #options = menu.option_set.all()
#     options = menu.options.all()  # MenuOption을 통해 연결된 Option 객체들을 가져옴
#     return render(request, 'kiosk/option.html', {'menu': menu, 'options': options})
#     #return render(request, 'kiosk/option.html', {'options': options})
#     # 옵션 데이터를 JSON 형식으로 응답
#     #return JsonResponse({'options': list(options.values('option'))})

# def menu_options(request, menu_id):
#     # Retrieve the menu item based on the menu ID
#     menu = Menu.objects.get(pk=menu_id)
#     # Retrieve the options associated with the menu item
#     #options = menu.option_set.all()
#     options = menu.options.all()
#     return render(request, 'kiosk/option.html', {'menu': menu, 'options': options})

# def menu_options(request, menu_id):
#     # Retrieve the menu item based on the menu ID
#     menu = Menu.objects.get(pk=menu_id)
#     # Retrieve the options associated with the menu item
#     options = menu.option_set.all()
#     return render(request, 'kiosk/option.html', {'menu': menu, 'options': options})