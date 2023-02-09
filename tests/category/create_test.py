import pytest
from django.urls import reverse
from rest_framework import status

from goals.serializers import GoalCategorySerializer


@pytest.mark.django_db
def test_create_category(user_factory, auth_client, board_participant_factory):
    user = user_factory()
    board_participant = board_participant_factory(user=user)

    data = {
        'board': board_participant.board.id,
        'title': 'test category',
    }

    get_auth_client = auth_client(user)
    url = reverse('category_create')
    response = get_auth_client.post(
        path=url,
        data=data,
    )

    assert response.status_code == 201

    expected_response = {
        'id': response.data['id'],
        'title': 'test category',
        'is_deleted': False,
        'board': board_participant.board.id,
        'created': response.data['created'],
        'updated': response.data['updated'],
    }

    assert response.data == expected_response


@pytest.mark.django_db
def test_goal_category_list(user_factory, auth_client, board_participant_factory, goal_category_factory):
    user = user_factory()
    board_participant = board_participant_factory(user=user)
    categories = goal_category_factory.create_batch(
        10, board=board_participant.board, user=user
    )

    get_auth_client = auth_client(user)
    url = reverse('category_list')
    response = get_auth_client.get(path=url)

    assert response.status_code == 200
    assert len(response.data) == 10
