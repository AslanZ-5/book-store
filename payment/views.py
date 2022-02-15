import stripe 

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from basket.basket import Basket


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)
    stripe.api_key = 'pk_test_51KTPH3Hhpp9pM3a6NdazrbU7xMfk6lYOMP1ug9mPmqiXowuRxn3W0Y7hHEbBKJDVUJh0LUgZqqkC61RHu1CshP9s00P2E0EUXX'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )
    return render(request, 'payment/pay_home.html', {'total': total})
