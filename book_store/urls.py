from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('admin/', admin.site.urls),

    path('__debug__/', include('debug_toolbar.urls')),
    
]

urlpatterns += i18n_patterns(
    path('', include('store.urls',namespace='store')),
    path('basket/',include('basket.urls',namespace='basket')),
    path('account/',include('account.urls',namespace='account')),
    path('checkout/', include("checkout.urls",namespace='checkout')),
    path('orders/',include('orders.urls',namespace='orders')),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
