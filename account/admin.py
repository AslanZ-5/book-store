from django.contrib import admin
from .models import Customer, Address


admin.site.register(Address)

@admin.register(Customer)
class adminRegister(admin.ModelAdmin):
    list_display = ('name','email')
    list_display_links = ('name','email')
