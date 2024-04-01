from mongoengine import Document, StringField, IntField, DateTimeField, BooleanField


class Requests(Document):
    phone_number = StringField(required=True)
    code = IntField(required=True)
    created = DateTimeField(required=True)
    expire = DateTimeField(required=True)
    request_limit = IntField(default=0)
    active = BooleanField(default=True)

