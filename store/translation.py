from modeltranslation.translator import register, TranslationOptions
from .models import (
                    Category,
                    Product,
                    ProductImage,
                    ProductSecification,
                    ProductSpecificationValue,
                    ProductType)

@register(Category)
class CategoryTranslateOptions(TranslationOptions):
    fields = ('name',)


@register(Product)
class CategoryTranslateOptions(TranslationOptions):
    fields = ('title', 'description')

@register(ProductType)
class CategoryTranslateOptions(TranslationOptions):
    fields = ('name',)

@register(ProductSecification)
class CategoryTranslateOptions(TranslationOptions):
    fields = ('name',)
    
@register(ProductImage)
class CategoryTranslateOptions(TranslationOptions):
    fields = ('alt_text',)



