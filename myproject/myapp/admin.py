from django.contrib import admin
from myapp.models import Customer, Item, OrderItem, Invoice

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display=['title','unit','unit_price','description']
admin.site.register(Item, ItemAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display=['item','quantity']
    list_display_links=['item']
    list_editable=['quantity']
admin.site.register(OrderItem, OrderItemAdmin)

class InvoiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Invoice, InvoiceAdmin)