from django.urls import path
from shopping_cart import views as shopping_cart_views

app_name = 'shopping_cart'

urlpatterns = [
    path(
        'add-to-cart/<slug:book_slug>/', 
        shopping_cart_views.AddToCartView.as_view(),
        name='add-to-cart'
    ),
    path(
        'remove-from-cart/<slug:book_slug>/', 
        shopping_cart_views.RemoveFromCartView.as_view(),
        name='remove-from-cart'
    ),
    path(
        'order-summary/',
        shopping_cart_views.OrderSummaryView.as_view(),
        name='order-summary'
    ),
    path(
        'checkout/',
        shopping_cart_views.CheckOutView.as_view(),
        name='checkout'
    )
]
