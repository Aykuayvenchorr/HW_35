import pytest
from django.urls import reverse
from rest_framework import status
import datetime

test_date = str(datetime.datetime.now().date())


@pytest.mark.django_db
def test_goal_update(user_factory, auth_client, board_participant_factory, goal_factory):
    user = user_factory()
    board_participant = board_participant_factory(user=user)
    goal = goal_factory(
        category__board=board_participant.board, category__user=user, user=user
    )

    data = {
        'category': goal.category_id,
        'title': 'test goal!',
        'description': 'desc',
        'due_date': "2023-02-08"
    }

    get_auth_client = auth_client(user)
    url = reverse('goal', kwargs={'pk': goal.id})
    response = get_auth_client.put(path=url, data=data)

    expected_response = {
        'id': goal.id,
        'title': 'test goal!',
        'category': goal.category_id,
        'description': 'desc',
        'due_date': "2023-02-08",
        'status': 1,
        'priority': 2,
        'created': goal.created.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        'updated': response.data['updated'],
        'user': {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        },
    }

    # assert response.status_code == 200
    assert response.data == expected_response
