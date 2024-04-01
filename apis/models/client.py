from django.db import models
from apis.models.abstract import TimeStampedModel, PersonalInformationModel
from apis.models.business import Shop, CustomerGroup
from apis.models.product import Article


class Person(TimeStampedModel):
    phone_number = models.CharField(max_length=20, unique=True, null=False, blank=False)

    def __str__(self):
        return self.phone_number


class Customer(TimeStampedModel, PersonalInformationModel):
    customer_group = models.ForeignKey(CustomerGroup, on_delete=models.CASCADE, related_name='customers', null=True,
                                       blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, to_field='id', related_name='customers')
    representative_user = models.BigIntegerField(null=True, blank=True)
    favorite_color = models.CharField(max_length=150, null=True, blank=True)
    point = models.IntegerField(null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE,related_name="customers")


    def __str__(self):
        return self.person.phone_number


class Cart(TimeStampedModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='carts')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='carts')

    def __str__(self):
        return self.customer.person.phone_number


class Buy(TimeStampedModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='buys')
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
