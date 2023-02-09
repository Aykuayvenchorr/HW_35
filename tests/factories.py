import factory
import datetime
from django.utils import timezone

# factory.Faker._DEFAULT_LOCALE='ru-RU'
from core.models import User
from goals.models import GoalCategory, Board, Goal, BoardParticipant, GoalComment
# test_date = str(datetime.datetime.now().date())

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = factory.Faker("password")


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    title = factory.Faker("sentence", nb_words=5)


class BoardParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BoardParticipant

    board = factory.SubFactory(BoardFactory)
    user = factory.SubFactory(UserFactory)


class GoalCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalCategory

    board = factory.SubFactory(BoardFactory)
    title = factory.Faker("sentence", nb_words=5)
    user = factory.SubFactory(UserFactory)


class GoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Goal

    title = factory.Faker("sentence", nb_words=5)
    category = factory.SubFactory(GoalCategoryFactory)
    user = factory.SubFactory(UserFactory)
    due_date = "2023-02-08"
    created = factory.LazyFunction(timezone.now)
    updated = factory.LazyFunction(timezone.now)


class GoalCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalComment

    user = factory.SubFactory(UserFactory)
    goal = factory.SubFactory(GoalFactory)
    text = factory.Faker("sentence", nb_words=5)
