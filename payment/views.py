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
    print('total')

    stripe.api_key = 'sk_test_51KTPH3Hhpp9pM3a695a4HMHZ8kGTR0YoWP665LWzPhOLsff3KcNsiUMhWsgZ0iHqJBvNMQvppT0DLpViGVn4jsNp00DWAM4oJU'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )
    return render(request, 'payment/pay_home.html', {'client_secret': intent.client_secret})

