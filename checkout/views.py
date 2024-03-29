import json
from paypalcheckoutsdk.orders import OrdersGetRequest
from .paypal import PayPalClient

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from orders.models import Order, OrderItem
from account.models import Address
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
        response = JsonResponse({'total':update_total_price, 'delivery_price':delivery_type.delivery_price})
        return response

@login_required
def delivery_address(request):
    session = request.session
    if 'purchase' not in request.session:
        messages.success(request, _("Please select delivery option"))
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
    addresses = Address.objects.filter(customer=request.user).order_by('-default')
    if addresses.exists():    
        if 'address' not in request.session:
            session['address'] = {'address_id': str(addresses[0].id)}
        else:
            session['address']['address_id'] = str(addresses[0].id)
            session.modified = True
    else:
        messages.error(request,"Please add address you don't have any address!")
        return redirect('account:add_address')
    return render(request, 'delivery_address.html', {"addresses":addresses})

@login_required
def payment_selection(request):
    if 'address' not in request.session:
        messages.success(request, "Please select delivery option")
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    return render(request,'payment_selection.html')

@login_required
def payment_complete(request):
    PPClient = PayPalClient()

    body = json.loads(request.body)
    data = body["orderID"]
    user_id = request.user.id

    requestorder = OrdersGetRequest(data)
    response = PPClient.client.execute(requestorder)

    total_paid = response.result.purchase_units[0].amount.value

    basket = Basket(request)
    order = Order.objects.create(
        user_id=user_id,
        full_name=response.result.purchase_units[0].shipping.name.full_name,
        email=response.result.payer.email_address,
        address1=response.result.purchase_units[0].shipping.address.address_line_1,
        address2=response.result.purchase_units[0].shipping.address.admin_area_2,
        postal_code=response.result.purchase_units[0].shipping.address.postal_code,
        country_code=response.result.purchase_units[0].shipping.address.country_code,
        total_paid=response.result.purchase_units[0].amount.value,
        order_key=response.result.id,
        payment_option="paypal",
        billing_status=True,
    )
    order_id = order.pk

    for item in basket:
        OrderItem.objects.create(order_id=order_id, product=item["product"], price=item["price"], quantity=item["qty"])

    return JsonResponse("Payment completed!", safe=False)

@login_required
def payment_successful(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment_successful.html', {})