from django.contrib.auth.models import Group, Permission
from rest_framework import serializers

from apis.models.business import Shop, Gift, Discount, CustomUser
from apis.models.client import Customer, Cart, Buy
from apis.models.product import ArticleGroup, Article, Ads


class CartSerializer(serializers.ModelSerializer):
    shop = serializers.CharField()
    customer = serializers.CharField()

    class Meta:
        model = Cart
        exclude = ['created', 'modified']


class CustomerSerializer(serializers.ModelSerializer):
    shop = serializers.CharField()
    person = serializers.CharField()
    customer_group = serializers.CharField()
    carts = CartSerializer(many=True)

    class Meta:
        model = Customer
        exclude = ['created', 'modified']


# class CustomerGroupSerializer(serializers.ModelSerializer):
#     customers = CustomerSerializer(many=True)
#     shop = serializers.CharField()
#     class Meta:
#         model = CustomerGroup
#         exclude = ['created', 'modified']
#

class ShopSerializer(serializers.ModelSerializer):
    owner = serializers.CharField()

    class Meta:
        model = Shop
        exclude = ['created', 'modified']


class UserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    shop = serializers.CharField()

    # user_permissions = UserPermissionsSerializer(many=True)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'shop', 'email', 'is_active']
        # fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    # shops = ShopSerializer(many=True)
    user_set = AdminSerializer(many=True)
    owners = user_set

    class Meta:
        model = Group
        fields = ['user_set', 'owners']


class GiftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gift
        exclude = ['created', 'modified', 'url']


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        exclude = ['created', 'modified']


#
# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         exclude = ['created', 'modified']


class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        exclude = ['created', 'modified']


class ArticleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleGroup
        exclude = ['created', 'modified']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['created', 'modified']


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        exclude = ['created', 'modified']


class WelcomeMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'welcome_message']
