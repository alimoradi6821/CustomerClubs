from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.business import Discount, Gift, CustomerGroup, Shop, CustomUser, Credit
from .models.client import Buy, Cart, Person, Customer
from .models.product import Article, ArticleGroup, Ads
from .models.project import SocialNetwork


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('shop', 'phone_number')
        })
    )


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Article)
admin.site.register(ArticleGroup)
admin.site.register(Buy)
admin.site.register(Cart)
admin.site.register(Person)
admin.site.register(Discount)
admin.site.register(Gift)
admin.site.register(Customer)
admin.site.register(CustomerGroup)
admin.site.register(Shop)
admin.site.register(SocialNetwork)
admin.site.register(Ads)
admin.site.register(Credit)
