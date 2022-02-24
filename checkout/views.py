from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import DeliveryOptions

@login_required
def deliverychoices(request):
    deliveryoptions = DeliveryOptions.objects.filter(is_active=True)
    return render(request, 'delivery_choices.html', {'deliveryoptions':deliveryoptions})


