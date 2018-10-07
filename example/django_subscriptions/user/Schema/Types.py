import graphene
from graphene_django import DjangoObjectType

from user.models import UserModel


# User Type
class User(DjangoObjectType):
    class Meta:
        model = UserModel
