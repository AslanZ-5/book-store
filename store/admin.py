from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import (Category,
                     Product,
                     ProductImage,
                     ProductSecification,
                     ProductSpecificationValue,
                     ProductType,
                     )
admin.site.register(Category, MPTTModelAdmin)



class ProductSpecificationInline(admin.TabularInline):
    model = ProductSecification

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name' ]
    inlines = [ 
        ProductSpecificationInline
    ]

class ProductImageInline(admin.TabularInline):
    model = ProductImage
class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title' ]
    list_display_links = ['title']
    inlines = [
        ProductSpecificationValueInline,
        ProductImageInline,
        

    ]

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_diplay = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name', )}


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
#     list_filter = ['in_stock', 'is_active']
#     list_editable = ['price', 'in_stock']
#     prepopulated_fields = {'slug': ('title', )}
