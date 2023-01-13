import uuid
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from books.models import Author, Book, UserLibrary
from home.models import CustomUser

def create_author_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Author.objects.filter(slug=slug).order_by('pk')
    exists = qs.exists()
    if exists:
        uuid_start = str(uuid.uuid1()).split("-", 1)[0] 
        new_slug = "%s-%s" %(slug, uuid_start)
        return create_author_slug(instance, new_slug=new_slug)

    return slug


def create_book_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Book.objects.filter(slug=slug).order_by('pk')
    exists = qs.exists()
    if exists:
        uuid_start = str(uuid.uuid1()).split("-", 1)[0] 
        new_slug = "%s-%s" %(slug, uuid_start)
        return create_book_slug(instance, new_slug=new_slug)

    return slug

@receiver(pre_save, sender=Author)
def pre_save_author_slug_reciever(sender, instance, **kwargs):
    try:
        author = Author.objects.get(pk=instance.pk)
        if instance.name != author.name:
            instance.slug = create_author_slug(instance)
        elif not instance.slug:
            instance.slug = create_author_slug(instance)
    except Author.DoesNotExist:
        pass
    

@receiver(pre_save, sender=Book)
def pre_save_book_slug_reciever(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_book_slug(instance)
    # try:
    #     book = Book.objects.get(pk=instance.pk)
    #     if instance.name != book.name:
    #         instance.slug = create_slug(instance)
    #     elif not instance.slug:
    #         instance.slug = create_slug(instance)
    # except Book.DoesNotExist:
    #     pass
    

@receiver(post_save, sender=CustomUser)
def post_save_user_library_receiver(sender, instance, created, **kwargs):
    if created:
        UserLibrary.objects.get_or_create(user=instance)