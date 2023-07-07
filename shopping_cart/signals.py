import uuid
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


from shopping_cart.models import Order


def generate_ref_no(instance, new_ref_no=None):
    """
    This function recursively generates a unique reference number
    """
    if new_ref_no is not None:
        ref_no = new_ref_no
    random_str = str(uuid.uuid1()).split("-", 1)[0]
    ref_no = f"digitalmarketplace-{random_str}"
    qs = Order.objects.filter(ref_code=ref_no).order_by('pk')
    if qs.exists():
        new_random_str = str(uuid.uuid1()).split("-", 1)[0] 
        new_ref_no = f"digitalmarketplace-{new_random_str}"
        return generate_ref_code(instance, new_ref_no=new_ref_no)

    return ref_no


@receiver(signal=post_save, sender=Order)
def generate_ref_code(sender, instance, **kwargs):
    if not instance.ref_code:
        instance.ref_code = generate_ref_no(instance)
        instance.save()
        print(instance)
