import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_goal_category_detail(user_factory, auth_client, board_participant_factory, goal_category_factory):
    user = user_factory()
    board_participant = board_participant_factory(user=user)
    category = goal_category_factory(board=board_participant.board, user=user)

    expected_response = {
        'id': category.id,
        'title': category.title,
        'is_deleted': False,
        'board': board_participant.board.id,
        'created': category.created.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        'updated': category.created.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        'user': {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        },
    }

    get_auth_client = auth_client(user)
    url = reverse('category', kwargs={'pk': category.pk})
    response = get_auth_client.get(path=url)

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_goal_category_detail_with_not_auth_user(user_factory, client, board_participant_factory, goal_category_factory):
    user = user_factory()
    board_participant = board_participant_factory(user=user)
    category = goal_category_factory(board=board_participant.board, user=user)
    url = reverse('category', kwargs={'pk': category.pk})
    response = client.get(path=url)

    assert response.status_code == 403
    assert response.data == {
        'detail': 'Authentication credentials were not provided.'
    }
