import uuid
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView, View, TemplateView
from books.models import Book
from shopping_cart.models import Order, OrderItem, Payment
from digital_marketplace.utils.choices import OrderStatus
# Create your views here.


class AddToCartView(LoginRequiredMixin, View):

    def get(self, request, book_slug):
        book = get_object_or_404(Book, slug=book_slug)
        order_item, created = OrderItem.objects.get_or_create(book=book)
        order, created = Order.objects.get_or_create(user=request.user, status=OrderStatus.Pending)
        order.items.add(order_item)
        order.save()

        return redirect(request.META.get('HTTP_REFERER'))
    

class RemoveFromCartView(LoginRequiredMixin, View):

    def get(self, request, book_slug):
        book = get_object_or_404(Book, slug=book_slug)
        order_item = get_object_or_404(OrderItem, book=book)
        order = get_object_or_404(Order, user=request.user, status=OrderStatus.Pending)
        order.items.remove(order_item)
        order.save()

        return redirect(request.META.get('HTTP_REFERER'))
    

class OrderSummaryView(LoginRequiredMixin, TemplateView):
    template_name = 'shopping_cart/order_summary.html'

    # def get_object(self):
    #     object = get_object_or_404(Order, user=self.request.user, status=OrderStatus.Pending)
    #     return object
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = None
        try:
            order = Order.objects.get(user=self.request.user, status=OrderStatus.Pending)
        except:
            pass
        ref_code = str(uuid.uuid1()).split("-", 1)[0] 
        
        context.update({
            'order': order,
            'ref_code':f"digitalmarketplace-{ref_code}"
        })
        return context
    

class CheckOutView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, user=self.request.user,status=OrderStatus.Pending)
        order.ref_code = str(uuid.uuid1()).split("-", 1)[0] 

        """
            do flutterwave stuff
        """

        payment = Payment()
        payment.order = order
        payment.transaction_ref = request.GET.get('tx_ref')
        payment.transaction_id =request.GET.get('transaction_id')
        payment.total_amount = order.get_total()
        payment.save()


        books_in_order = [item.book for item in order.items.all()]
        for book in books_in_order:
            request.user.userlibrary.books.add(book)
        
        order.status = OrderStatus.Completed
        order.save()

        messages.success(request, "Payment made successfully")
        return redirect("books:book-list")
    # def get(self, request, *args, **kwargs):
    #     
    #     order.status = OrderStatus.Completed
    #     OrderStatus.save()
    #     return rend