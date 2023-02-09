import datetime

import pytest
from django.urls import reverse
from rest_framework import status


# from goals.serializers import GoalSerializer

# test_date = str(datetime.datetime.now().date())
@pytest.mark.django_db
def test_create_goal(user_factory, auth_client, goal_category_factory, board_participant_factory):
    user = user_factory()
    board_participant = board_participant_factory(user=user)
    category = goal_category_factory(board=board_participant.board, user=user)
    data = {
        'category': category.id,
        'title': 'test goal',
        'description': 'test',
        'due_date': "2023-02-08",
    }

    get_auth_client = auth_client(user)
    url = reverse('goal_create')
    response = get_auth_client.post(
        path=url,
        data=data,
    )
    expected_response = {
        'id': response.data['id'],
        'category': category.id,
        'title': 'test goal',
        'description': 'test',
        'priority': 2,
        'status': 1,
        'due_date': "2023-02-08",
        'created': response.data['created'],
        'updated': response.data['updated'],
    }
    assert response.data == expected_response
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_goal_list(user_factory, auth_client, board_participant_factory, goal_factory):
    user = user_factory()
    board_participant = board_participant_factory(user=user)
    goals = goal_factory.create_batch(
        10,
        category__board=board_participant.board,
        category__user=user,
        user=user,
    )

    get_auth_client = auth_client(user)
    url = reverse('goal_list')
    response = get_auth_client.get(path=url)

    assert response.status_code == 200
    assert len(response.data) == 10
