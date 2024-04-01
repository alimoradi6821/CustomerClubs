from django.db import models
from apis.models.abstract import BaseModel, TimeStampedModel
from apis.models.business import Shop, Discount, CustomerGroup
from apis.models.project import SocialNetwork


class ArticleGroup(TimeStampedModel, BaseModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='article_groups')
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='article_groups')


class Article(TimeStampedModel, BaseModel):
    price = models.CharField(max_length=150)
    point = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='articles')
    article_group = models.ForeignKey(ArticleGroup, on_delete=models.CASCADE, related_name='articles', null=True,
                                      blank=True)


class Ads(TimeStampedModel, BaseModel):
    file = models.FileField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    customer_group = models.ForeignKey(CustomerGroup, on_delete=models.CASCADE, related_name='ads')
    social_network = models.ManyToManyField(SocialNetwork)
