from mongoengine import Document, IntField, DateTimeField, BooleanField ,FloatField

from apis.models.abstract import TimeStampedModel, BaseModel


class Message(Document):
    time = DateTimeField(required=True)
    ads_id = IntField(required=True)
    active = BooleanField(default=True)


class NewCustomer(Document):
    ads_id = IntField(required=True)
    active = BooleanField(default=True)


class AfterBuy(Document):
    ads_id = IntField(required=True)
    active = BooleanField(default=True)


class SocialNetwork(TimeStampedModel, BaseModel):
    pass
