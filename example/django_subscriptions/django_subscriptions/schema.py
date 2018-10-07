import graphene

from .Schema.Query import GetUsersQuery
from .Schema.Mutation import CreateUserMutation
from .Schema.Subscription import NewUsersSubscription


class Query(
    GetUsersQuery,
    graphene.ObjectType,
):
    """Root GraphQL Query."""
    pass


class Mutation(graphene.ObjectType):
    """Root GraphQL Mutation."""
    create_user = CreateUserMutation.Field()


class Subscription(graphene.ObjectType):
    """Root GraphQL subscription."""
    new_users_subscription = NewUsersSubscription.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription,
)
