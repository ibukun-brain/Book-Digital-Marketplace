import json
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import View, TemplateView

from books.models import Book
from shopping_cart.models import Order, OrderItem, Payment

from digital_marketplace.utils.choices import OrderStatus
from digital_marketplace.utils.hash import shaEncryption
from digital_marketplace.utils.env_variable import get_env_variable
from digital_marketplace.utils.api import verify_user_transactions
from digital_marketplace.utils.choices import PaymentStatus

# Create your views here.


class AddToCartView(LoginRequiredMixin, View):

    def get(self, request, book_slug):
        book = get_object_or_404(Book, slug=book_slug)
        order_item, created = OrderItem.objects.get_or_create(book=book)
        order, _ = Order.objects.get_or_create(user=request.user, status=OrderStatus.Pending)
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
        request = self.request
        order = None
        try:
            order = Order.objects.get(user=self.request.user, status=OrderStatus.Pending)
        except:
            pass
        secret_key = get_env_variable('FLUTTERWAVE_SECRET_KEY')
        hashed_secret_key = shaEncryption(secret_key)
        string_to_be_hashed = (
            str(order.get_total()) + "NGN" + request.user.email + order.ref_code + hashed_secret_key
        )
        payload_hash = shaEncryption(string_to_be_hashed)
        public_key = get_env_variable('FLUTTERWAVE_PUBLIC_KEY')

        context.update({
            'order': order,
            'public_key': public_key,
            'ref_code': order.ref_code,
            'payload_hash': payload_hash
        })
        return context
    

class CheckOutView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, user=self.request.user,status=OrderStatus.Pending)

        """
            do flutterwave stuff
        """

        payment, _ = Payment.objects.get_or_create(order=order)
        transaction_id = request.GET.get('transaction_id')
        payment.transaction_id = transaction_id
        payment.total_amount = order.get_total()
        payment.save()
        response = verify_user_transactions(transaction_id)

        if response['data']['status'] == 'successful' and \
        response['data']['amount'] == order.get_total() and \
        response['data']['currency'] == 'NGN':
            payment.status = PaymentStatus.Successful
            payment.raw_response = response
            payment.save()

            books_in_order = [item.book for item in order.items.all()]
            for book in books_in_order:
                request.user.userlibrary.books.add(book)
            
            order.status = OrderStatus.Completed
            order.save()

            messages.success(request, "Payment made successfully")
            return redirect("books:book-list")
    
            
        payment.status = PaymentStatus.Failed
        payment.save()
        messages.error(request, "Payment failed")
        return redirect("books:book-list")


@require_POST
@csrf_exempt
def webhook(request):
    secret_hash = get_env_variable("FLUTTERWAVE_SECRET_HASH")
    signature = request.headers.get("Verif-Hash")
    if signature is None or signature != secret_hash:
        return HttpResponse(status=401)
    payload = json.loads(request.body)
    existing_payment = Payment.objects.get(transaction_id=payload.get('id'))
    if existing_payment.status == payload.get('status'):
        return HttpResponse(status=200)
    existing_payment.status = payload.get('status')
    existing_payment.save()
    HttpResponse(status=200)