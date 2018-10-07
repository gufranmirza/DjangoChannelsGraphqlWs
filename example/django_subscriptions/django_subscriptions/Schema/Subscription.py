import graphene
import channels_graphql_ws

# Import Models
from user.models import UserModel

# Import Types
from user.Schema.Types import User


class NewUsersSubscription(channels_graphql_ws.Subscription):
    """Simple GraphQL subscription."""

    # Subscription payload.
    user = graphene.Field(User)

    class Arguments:
        """That is how subscription arguments are defined."""
        arg1 = graphene.String()
        arg2 = graphene.String()

    @staticmethod
    def subscribe(root, info, arg1, arg2):
        """Called when user subscribes."""

        # Return the list of subscription group names.
        return ['group42']

    @staticmethod
    def publish(user_id, info, arg1, arg2):
        """Called to notify the client."""

        # Here `payload` contains the `payload` from the `broadcast()`
        # invocation (see below). You can return `MySubscription.SKIP`
        # if you wish to suppress the notification to a particular
        # client. For example, this allows to avoid notifications for
        # the actions made by this particular client.

        user = UserModel.objects.get(id=user_id)

        return NewUsersSubscription(user=user)
