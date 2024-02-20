import os
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Store, Menu, Option, OptionContent, Cart, Order
from django.db.models import Sum
from google.cloud import speech_v1
from google.oauth2 import service_account
from django.http import JsonResponse
from django.conf import settings
from random import choice

# Create your views here.
def landing(request):
    return render(request, 'kiosk/landing.html', {})

def search_or_browse(request):
    return render(request, 'kiosk/search_or_browse.html', {})

def search(request):
    return render(request, 'kiosk/search.html', {})

def menu(request):
    items_per_page = 10
    # Menu 모델에서 모든 메뉴를 가져옵니다.
    all_menus = Menu.objects.all()
    paginator = Paginator(all_menus, items_per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Menu 모델에서 모든 고유한 카테고리를 가져옵니다.
    categories = Menu.objects.values_list('category', flat=True).distinct()

    # 가장 작은 menuId를 가지고 있는 카테고리를 가져옵니다.
    first_category = Menu.objects.order_by('menuId').first().category


    return render(request, 'kiosk/menu.html',
                  {'categories': categories, 'menus': page_obj, 'first_category': first_category})

def menu_options(request, menu_id):
    # Retrieve the menu item based on the menu ID
    menu = Menu.objects.get(pk=menu_id)
    # Retrieve the option IDs associated with the menu item
    option_ids = menu.optionId.all()
    # Retrieve the options based on the option IDs
    options = Option.objects.filter(pk__in=option_ids)

    return render(request, 'kiosk/option.html', {'menu': menu, 'options': options})


def convert_speech_to_text(request):

    if request.method == 'POST':
        # 클라이언트로부터 받은 음성 텍스트
        audio_text = request.POST.get('audio_text')

        # JSON 파일의 경로 설정
        json_file_path = os.path.join(settings.BASE_DIR, 'kiosk', 'solutionproject-414810-6aa45c89e5cc.json')

        # Google STT API 인증 정보
        credentials = service_account.Credentials.from_service_account_file(json_file_path)


        # Google STT 클라이언트 생성
        client = speech_v1.SpeechClient(credentials=credentials)

        # 음성 텍스트를 변환합니다.
        response = client.recognize({
            'config': {
                'encoding': 'LINEAR16',
                'sample_rate_hertz': 44100,
                'language_code': 'ko-KR',
            },
            'audio': {
                'content': audio_text,
            }
        })

        # 변환된 텍스트를 추출합니다.
        recognized_text = response.results[0].alternatives[0].transcript

        recognized_text = recognized_text.rstrip('.')

        return JsonResponse({'text': recognized_text})

def get_menu_id(request):
    if request.method == 'POST':
        transcription = request.POST.get('transcription', '')
        # Search for the Menu object based on the recognized text
        try:
            menus = Menu.objects.filter(name__icontains=transcription)
            if menus.exists():
                menu_ids = [menu.pk for menu in menus]
                return JsonResponse({'menu_ids': menu_ids})
            else:
                return JsonResponse({'error': 'Menu not found'}, status=404)
        except Menu.DoesNotExist:
            return JsonResponse({'error': 'Menu not found'}, status=404)
        else:
            return JsonResponse({'error': 'Invalid request method'}, status=405)


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

def add_to_cart(request):
    if request.method == 'POST':
        menu_id = request.POST.get('menu_id')
        selected_options = request.POST.getlist('selected_options[]')

        # 메뉴 객체 가져오기
        menu = Menu.objects.get(pk=menu_id)

        # 선택된 옵션 내용 가져오기
        selected_contents = OptionContent.objects.filter(content__in=selected_options)

        # 장바구니에 추가
        cart_item = Cart.objects.create(
            menuId=menu,
            price=menu.price,
            options=', '.join(selected_options)
        )

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})