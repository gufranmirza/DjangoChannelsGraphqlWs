import graphene

# Import Models
from user.models import UserModel

# Import Types
from user.Schema.Types import User

from .Subscription import NewUsersSubscription


class CreateUserMutation(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        name = graphene.String()
        last_name = graphene.String()

    def mutate(self, info, name, last_name):
        user = UserModel(name=name, last_name=last_name)
        user.save()

        NewUsersSubscription.broadcast(
            # Subscription group to notify clients in.
            group='group42',

            # Dict delivered to the `publish` method.
            # Can not pass objects, So pass id And resolve it on Subscription
            payload=user.id
        )

        return CreateUserMutation(
            user=user
        )
