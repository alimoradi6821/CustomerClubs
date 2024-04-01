from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['created']


class BaseModel(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class PersonalInformationModel(models.Model):
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    province = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    national_code = models.CharField(max_length=150, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    home_phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    job = models.CharField(max_length=150, null=True, blank=True)
    card_number = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

