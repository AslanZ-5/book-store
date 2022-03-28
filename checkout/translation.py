from modeltranslation.translator import register, TranslationOptions
from .models import DeliveryOptions

@register(DeliveryOptions)
class CategoryTranslateOptions(TranslationOptions):
    fields = ('delivery_name','delivery_timeframe','delivery_window')