from django.contrib import admin
from shopping_cart.models import Order, OrderItem, Payment

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'created_at', 'ref_code']
    list_select_related = ['user']
    search_fields = ['user__username', 'ref_code', 'items__name']
    list_filter = ['status', 'created_at', 'updated_at']
    filter_horizontal = ['items']
    date_hierarchy = 'created_at'
    autocomplete_fields = ['user']



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['book', 'created_at']
    list_select_related = ['book']
    list_filter = ['created_at', 'updated_at']
    autocomplete_fields = ['book']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order', 'total_amount', 'transaction_id', 'transaction_ref']
    list_select_related = ['order']
    list_filter = ['created_at', 'updated_at']
    autocomplete_fields = ['order']
