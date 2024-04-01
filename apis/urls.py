from django.urls import include, path
from rest_framework import routers

from apis import views

router = routers.DefaultRouter()
router.register(r'owner', views.OwnerViewSet)
router.register(r'admin', views.AdminViewSet)
router.register(r'ads', views.AdsViewSet, basename='ads')
router.register(r'welcome_msg', views.WelcomeMessageViewSet, basename='welcome_msg')
router.register(r'shop', views.ShopViewSet, basename="shop")
router.register(r'username_login', views.LogInOwnerWithUsernamePassword, basename='username_login')
router.register(r'phone_number_login', views.LogInOwnerWithPhoneNumber, basename='phone_number_login')
router.register(r'check_code', views.CheckLoginCode, basename='check_code')
# router.register(r'customer_group', views.CustomerGroupViewSet)
router.register(r'customer', views.CustomerViewSet, basename='customer')
router.register(r'gift', views.GiftViewSet)
router.register(r'discount', views.DiscountViewSet)
# router.register(r'person', views.PersonViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'buy', views.BuyViewSet)
router.register(r'article_group', views.ArticleGroupViewSet)
router.register(r'article', views.ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
