from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("User"))
    is_paid = models.BooleanField(_("Is Paid?"), default=False)

    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    phone_number = models.CharField(_("Phone Number"), max_length=11)
    address = models.CharField(_("Address"), max_length=200)
    order_notes = models.CharField(_("Order Notes"), max_length=350, blank=True)

    zarinpal_authority = models.CharField(max_length=255, blank=True)
    zarinpal_ref_id = models.CharField(max_length=150, blank=True)
    zarinpal_data = models.TextField(blank=True)

    datetime_created = models.DateTimeField(_("Created"), auto_now_add=True)
    date_modified = models.DateTimeField(_("Modified"), auto_now=True)

    def __str__(self):
        return f"Order {self.id}"

    def get_total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'OrderItem {self.id}: {self.product} x {self.quantity} (price:{self.price})'
