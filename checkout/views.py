from urllib import response
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from basket.basket import Basket
from .models import DeliveryOptions

@login_required
def deliverychoices(request):
    deliveryoptions = DeliveryOptions.objects.filter(is_active=True)
    return render(request, 'delivery_choices.html', {'deliveryoptions':deliveryoptions})

@login_required
def basket_update_delivery(request):
    basket = Basket(request)

    if request.POST.get("action") == 'post':
        delivery_option = int(request.POST.get("deliveryoption"))
        delivery_type = DeliveryOptions.objects.get(id=delivery_option)
        update_total_price = basket.basket_update_delivery(delivery_type.delivery_price)

        session = request.session
        if 'purchase' not in request.session:
            session['purchase'] = {
                'delivery_id': delivery_type.id,
            }
        else:
            session['purchase']['delivery_id'] = delivery_type.id
            session.modified = True 
        response = JsonResponse({'hell':'hellkk1221','total':update_total_price, 'delivery_price':delivery_type.delivery_price})
        return response