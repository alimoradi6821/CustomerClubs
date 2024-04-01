from django.conf import settings
from django.db import models
from apis.models.abstract import TimeStampedModel, BaseModel
from django.contrib.auth.models import AbstractUser


class Shop(TimeStampedModel, BaseModel):
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    site = models.CharField(max_length=250, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shops')
    welcome_message = models.TextField(null=True, blank=True)


class Credit(TimeStampedModel):
    message = models.IntegerField()
    customer = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='credits')


class CustomerGroup(TimeStampedModel, BaseModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, to_field='id', related_name='customer_groups')

    def __str__(self):
        return self.name


class Gift(TimeStampedModel):
    GIFT_TYPES = (
        (0, 'discount'),
        (1, 'point'),
        (2, 'ben'),
        (3, 'other'),
    )
    type = models.IntegerField(choices=GIFT_TYPES)
    amount = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='gifts')
    customer_group = models.ForeignKey(CustomerGroup, on_delete=models.CASCADE, related_name='gifts')

    def __str__(self):
        return f"{self.amount} {self.GIFT_TYPES[self.type][1]} for {self.shop.name}"


class Discount(TimeStampedModel, BaseModel):
    amount = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='discounts')


class CustomUser(AbstractUser):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='admins', null=True, blank=True)
    phone_number = models.CharField(max_length=20, unique=True, null=False, blank=False)
