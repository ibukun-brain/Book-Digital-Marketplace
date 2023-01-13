from shopping_cart.models import Order, OrderItem
from digital_marketplace.utils.choices import BookStatus

def check_book_relationship(request, book):
    # if book in request.user.userlibrary.book_list()
    if book in request.user.userlibrary.books.all():
        return BookStatus.Owned
    
    order_qs = Order.objects.filter(user=request.user)
    if order_qs.exists():
        order = order_qs.first()
        order_item_qs = OrderItem.objects.filter(book=book)
        if order_item_qs.exists():
            order_item = order_item_qs.first()
            if order_item in order.items.all():
                return BookStatus.In_cart
            
    return BookStatus.Not_in_cart
