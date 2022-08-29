from django.contrib import admin
from .models import *

class MainAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
admin.site.register(Admin, MainAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('date_ordered',)
admin.site.register(Orders, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity',)
admin.site.register(Items, OrderItemAdmin)

class SpecialItemAdmin(admin.ModelAdmin):
    list_display = ('product',)
admin.site.register(Special, SpecialItemAdmin)

class ExclusiveItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'discount',)
admin.site.register(Exclusive, ExclusiveItemAdmin)
