import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apis.models.business import Shop, Gift, Discount, CustomUser, CustomerGroup
from apis.models.client import Customer, Person, Cart, Buy
from apis.models.login import Requests
from apis.models.product import ArticleGroup, Article, Ads
from apis.models.project import SocialNetwork
from apis.serialization import OwnerSerializer, ShopSerializer, CustomerSerializer, \
    GiftSerializer, DiscountSerializer, CartSerializer, BuySerializer, \
    ArticleGroupSerializer, ArticleSerializer, AdminSerializer, WelcomeMessageSerializer
from module.check import PhoneNumber, Parameters
from module.massage import E, R
from random import randint
from mongoengine import Q


class OwnerViewSet(viewsets.ViewSet):
    queryset = Group.objects.filter(name="owner")
    serializer_class = OwnerSerializer

    @staticmethod
    def list(request):
        queryset = Group.objects.filter(name="owner")
        serializer = OwnerSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request): pass


class ShopViewSet(viewsets.ViewSet):

    def list(self, request):
        admin = self.get_admin(request.user.id)
        if admin is None:
            return Response(E.not_found("owner"), status=status.HTTP_404_NOT_FOUND)

        queryset = Shop.objects.filter(owner=admin)
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        s, data = Parameters.is_required(request, "name", "owner")
        no_data = Parameters.non_required(request, "email", "phone_number", "site", "description")

        if s is False:
            return Response(data,
                            status=status.HTTP_400_BAD_REQUEST)

        if self.check_uniq_name(data["name"], data["owner"]) is False:
            return Response(E.ALREADY_EXIST,
                            status=status.HTTP_400_BAD_REQUEST)

        owner = self.check_is_owner(data["owner"])
        if owner is None:
            return Response(E.invalid("username"),
                            status=status.HTTP_400_BAD_REQUEST)
        data["owner"] = owner

        self.create_shop(data, no_data)
        return Response(R.CREATED, status=status.HTTP_200_OK)

    @staticmethod
    def check_uniq_name(n, o):

        if Shop.objects.filter(name=n, owner__username=o).first():
            return False

    @staticmethod
    def check_is_owner(o):
        user = CustomUser.objects.filter(username=o).first()
        if user:
            is_owner = user.groups.filter(name="owner").first()
            if is_owner:
                return user
            else:
                return None
        else:
            return None

    @staticmethod
    def create_shop(d, n):

        Shop.objects.create(name=d["name"], owner=d["owner"], email=n["email"], phone_number=n["phone_number"],
                            site=n["site"], description=n["description"])

    @staticmethod
    def get_admin(admin_id):
        admin = CustomUser.objects.filter(id=admin_id).first()
        if admin:
            return admin
        else:
            return None


# class CustomerGroupViewSet(viewsets.ModelViewSet):
#     queryset = CustomerGroup.objects.all()
#     serializer_class = CustomerGroupSerializer

class WelcomeMessageViewSet(viewsets.ViewSet):

    def list(self, request):
        admin = self.get_admin(request.user.id)
        if admin is None:
            return Response(E.not_found("owner"), status=status.HTTP_404_NOT_FOUND)

        queryset = Shop.objects.filter(owner=admin)
        serializer = WelcomeMessageSerializer(queryset, many=True)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        print(kwargs["pk"])
        admin = self.get_admin(request.user.id)
        if admin is None:
            return Response(E.not_found("owner"), status=status.HTTP_404_NOT_FOUND)
        for i in Shop.objects.filter(owner=admin):
            i.welcome_message = kwargs["pk"]
            i.save()
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def get_admin(admin_id):
        admin = CustomUser.objects.filter(id=admin_id).first()
        if admin:
            return admin
        else:
            return None


class CustomerViewSet(viewsets.ViewSet):

    def list(self, request):
        admin = self.get_admin(request.user.id)
        if admin is None:
            return Response(E.not_found("owner"), status=status.HTTP_404_NOT_FOUND)

        queryset = Customer.objects.filter(shop__owner=admin)
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):

        s, data = Parameters.is_required(request, "phone_number")
        if s is False:
            return Response(data,
                            status=status.HTTP_400_BAD_REQUEST)

        admin = self.get_admin(request.user.id)
        if admin is None:
            return Response(E.not_found("admin"), status=status.HTTP_404_NOT_FOUND)

        shop = admin.shop
        if shop is None:
            return Response(E.not_found("shop"), status=status.HTTP_404_NOT_FOUND)

        user = self.get_user(data['phone_number'])
        if user is None:
            return Response(E.invalid("phone number"), status=status.HTTP_400_BAD_REQUEST)

        s = self.create_customer(shop, user)
        if s is False:
            return Response(E.ALREADY_EXIST, status=status.HTTP_400_BAD_REQUEST)

        return Response({"msg": shop.welcome_message}, status=status.HTTP_201_CREATED)

    @staticmethod
    def get_user(pn):

        if PhoneNumber.is_valid(pn):
            user = Person.objects.get_or_create(phone_number=pn)[0]
            return user

        else:
            return None

    @staticmethod
    def create_customer(shop, person):

        if len(Customer.objects.filter(person=person, shop=shop)) > 0:
            return False
        else:
            Customer.objects.create(person=person, shop=shop)
            return True

    @staticmethod
    def get_admin(admin_id):
        admin = CustomUser.objects.filter(id=admin_id).first()
        if admin:
            return admin
        else:
            return None


class GiftViewSet(viewsets.ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class AdminViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = AdminSerializer


#
# class PersonViewSet(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class BuyViewSet(viewsets.ModelViewSet):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer


class ArticleGroupViewSet(viewsets.ModelViewSet):
    queryset = ArticleGroup.objects.all()
    serializer_class = ArticleGroupSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AdsViewSet(viewsets.ViewSet):

    def create(self, request):
        s, data = Parameters.is_required(request, "customer_group", "message", 'social_network', 'send_time')
        if s is False:
            return Response(data,
                            status=status.HTTP_400_BAD_REQUEST)
        no_data = Parameters.non_required(request, "file")
        self.create_ads(data, no_data)
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def create_ads(d, n):
        sn = SocialNetwork.objects.filter(name=d["social_network"]).first()
        if sn:
            cg = CustomerGroup.objects.filter(name=d["customer_group"]).first()
            if cg:
                ads = Ads.objects.create(file=n["file"], message=d["message"], customer_group=cg, social_network=sn)


class LogInOwnerWithUsernamePassword(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        s, data = Parameters.is_required(request, "username", "password")
        if s is False:
            return Response(data,
                            status=status.HTTP_400_BAD_REQUEST)

        user = self.get_user(u=data["username"], p=data["password"])
        if user is None:
            return Response(E.invalid("username or password"),
                            status=status.HTTP_401_UNAUTHORIZED)
        if self.is_owner(user) is False:
            return Response(E.PERMISSION_DENIED,
                            status=status.HTTP_401_UNAUTHORIZED)
        token = self.get_token(user)
        return Response({"token": token}, status=status.HTTP_200_OK)

    @staticmethod
    def get_user(u, p):
        user = authenticate(username=u, password=p)
        if user:
            return user

        else:
            return None

    @staticmethod
    def is_owner(u):
        group = u.groups.filter(name="owner").first()
        if group:
            return True
        else:
            return False

    @staticmethod
    def get_token(u):
        token = Token.objects.get_or_create(user=u)
        return str(token[0])


class LogInOwnerWithPhoneNumber(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        s, data = Parameters.is_required(request, "phone_number")
        if s is False:
            return Response(data,
                            status=status.HTTP_400_BAD_REQUEST)

        user = self.get_user(data["phone_number"])
        if user is None:
            return Response(E.invalid("phone number"),
                            status=status.HTTP_401_UNAUTHORIZED)
        code = self.login_request(user)

        return Response({"code": code}, status=status.HTTP_200_OK)

    @staticmethod
    def get_user(pn):

        if PhoneNumber.is_valid(pn):
            user = CustomUser.objects.filter(phone_number=pn).first()
            print(*CustomUser.objects.all())
            if user:
                return user
            else:
                return None
        else:
            return None

    def login_request(self, u):
        c, e = self.set_time()
        code = self.random_number(6)
        self.set_false_activate(u)
        req = Requests(phone_number=u.phone_number, code=code, created=c, expire=e)
        req.save()

        return code

    @staticmethod
    def random_number(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)

    @staticmethod
    def set_false_activate(u):
        for i in Requests.objects(phone_number=u.phone_number, active=True):
            i.active = False
            i.save()

    @staticmethod
    def set_time():

        created = datetime.datetime.now()

        expire = datetime.datetime.now() + datetime.timedelta(minutes=5)

        return created.strftime("%Y-%m-%d %H:%M:%S"), expire.strftime("%Y-%m-%d %H:%M:%S")


class CheckLoginCode(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):

        s, data = Parameters.is_required(request, "phone_number", "code")
        if s is False:
            return Response(data,
                            status=status.HTTP_400_BAD_REQUEST)

        if PhoneNumber.is_valid(data["phone_number"]) is False:
            return Response(E.invalid("phone number"),
                            status=status.HTTP_401_UNAUTHORIZED)

        if self.check_valid_code(data) is False:
            return Response(E.invalid("code"),
                            status=status.HTTP_401_UNAUTHORIZED)
        token = self.get_token(data["phone_number"])
        if token is None:
            return Response(E.not_found("token"),
                            status=status.HTTP_401_UNAUTHORIZED)

        return Response({"token": token}, status=status.HTTP_200_OK)

    def check_valid_code(self, p):

        self.increase_req_limit(p)
        code = Requests.objects(Q(request_limit__lte=5) & Q(active=True) & Q(code=int(p["code"])) & Q(
            phone_number=p["phone_number"]))

        if len(code) == 1:
            now_timedate_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            now_timedate = datetime.datetime.strptime(now_timedate_str, '%Y-%m-%d %H:%M:%S')

            if code[0]["expire"] > now_timedate:
                code[0]["active"] = False
                code[0].save()
                return True

            else:
                return False

        else:
            return False

    @staticmethod
    def get_token(p):
        token = Token.objects.filter(user__phone_number=p).first()
        if token:
            return token.key

        else:
            return None

    @staticmethod
    def increase_req_limit(p):
        req = Requests.objects.get(phone_number=p["phone_number"], active=True)
        req.request_limit += 1
        req.save()
