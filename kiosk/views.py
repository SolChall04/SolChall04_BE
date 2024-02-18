from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Store, Menu, Option, OptionContent, Cart, Order
from django.db.models import Sum
from django.http import JsonResponse


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


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        card = get_object_or_404(Cart, cartId=card_id)
        card.delete()


        carts = Cart.objects.all()
        total_quantity = len(carts)
        total_price = Cart.objects.aggregate(total_price=Sum('price'))['total_price']

        data_and_message = {
            'total_quantity' : total_quantity,
            'total_price' : total_price,
            'message' : '카트 삭제'
        }

        # 성공적으로 삭제되었다는 응답을 반환
        return JsonResponse(data_and_message)

    # POST 요청이 아닌 경우 에러 응답
    return JsonResponse({'error': '올바르지 않은 요청입니다.'}, status=400)



# 총 수량 계산 및 전송하는 함수
def cal_totalQuantity(t) :
    
    carts = Cart.objects.all()

    t = len(carts)
    return t

# 총 가격 계산 및 전송하는 함수
def cal_totalPrice(p) :

    p = Cart.objects.aggregate(total_price=Sum('price'))['total_price']
    return p