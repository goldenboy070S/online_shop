from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Order, Product
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Images
import os

@receiver(post_delete, sender=Images)
def delete_images_on_product_delete(sender, instance, **kwargs):
    for field in ['image1', 'image2', 'image3', 'image4', 'image5']:
        image_field = getattr(instance, field)
        if image_field and os.path.isfile(image_field.path):
            os.remove(image_field.path)


@receiver(post_save, sender=Order)
def update_product_quantities_on_order(sender, instance, created, **kwargs):
    # Faqat `status` 'Completed' bo'lganda ishlaydi
    if instance.status == 'Completed':
        # Faqat yangi yaratilgan yoki `status` o'zgargan holatlarni tekshiramiz
        if created or instance.tracker.has_changed('status'):  # `django-model-utils` kerak
            if instance.cart:
                for cart_item in instance.cart.cart_items.all():
                    product = cart_item.product
                    quantity_ordered = cart_item.quantity
                    if product.quantity < quantity_ordered:
                        raise ValidationError(
                            f"Not enough stock for {product.name}. Available quantity: {product.quantity}"
                        )
                    product.quantity -= quantity_ordered
                    product.save()
