import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from tests.factories import BoardFactory, GoalCategoryFactory, GoalFactory, GoalCommentFactory, BoardParticipantFactory


# USER_MODEL = get_user_model()


# @pytest.fixture
# def test_user():
#     user = USER_MODEL.objects.create(
#         username='test',
#         password='test',
#         email='test@mail.ru'
#     )
#     return user

# @pytest.fixture
# def auth_client(test_user):
# client = APIClient()
# client.force_authenticate(test_user)
# return client


@pytest.fixture
def auth_client(client):
    def _get_auth_client(user):
        client.force_login(user=user)
        return client

    return _get_auth_client


@pytest.fixture()
def client() -> APIClient:
    return APIClient()

#
# @pytest.fixture
# def board():
#     return BoardFactory.create()
#
#
# @pytest.fixture
# def board_list():
#     return BoardFactory.create_batch(size=10)
#
#
# @pytest.fixture
# def board_participant(test_user, board):
#     return BoardParticipantFactory.create(user=test_user, board=board, role=1)
#
#
# @pytest.fixture
# def goal_category(test_user, board):
#     return GoalCategoryFactory.create(user=test_user, board=board)
#
#
# @pytest.fixture
# def goal_category_list(test_user, board):
#     return GoalCategoryFactory.create_batch(size=10, user=test_user, board=board)
#
#
# @pytest.fixture
# def goal(test_user, goal_category):
#     return GoalFactory.create(user=test_user, category=goal_category)
#
#
# @pytest.fixture
# def goal_list(test_user, goal_category):
#     return GoalFactory.create_batch(size=10, user=test_user, category=goal_category)
#
#
# @pytest.fixture
# def goal_comment(test_user, goal):
#     return GoalCommentFactory.create(user=test_user, goal=goal)
#
#
# @pytest.fixture
# def goal_comment_list(test_user, goal):
#     return GoalCommentFactory.create_batch(size=10, user=test_user, goal=goal)
