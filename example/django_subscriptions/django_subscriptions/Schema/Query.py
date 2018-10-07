import graphene

# Import Models
from user.models import UserModel

# Import Types
from user.Schema.Types import User


class GetUsersQuery(graphene.ObjectType):
    get_users = graphene.List(User)

    def resolve_get_users(self, info):

        return UserModel.objects.all()
