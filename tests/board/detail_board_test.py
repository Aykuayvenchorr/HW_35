import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_board_detail(auth_client, board_participant):
    expected_response = {
        'id': board_participant.board.id,
        'title': board_participant.board.title,
        'is_deleted': False,
        'created': board_participant.board.created.strftime(
            '%Y-%m-%dT%H:%M:%S.%fZ'
        ),
        'updated': board_participant.board.created.strftime(
            '%Y-%m-%dT%H:%M:%S.%fZ'
        ),
        'participants': [
            {
                'id': board_participant.id,
                'role': board_participant.role,
                'user': board_participant.user.username,
                'created': board_participant.created.strftime(
                    '%Y-%m-%dT%H:%M:%S.%fZ'
                ),
                'updated': board_participant.updated.strftime(
                    '%Y-%m-%dT%H:%M:%S.%fZ'
                ),
                'board': board_participant.board.id,
            },
        ],
    }

    get_auth_client = auth_client(board_participant.user)
    url = reverse('board', kwargs={'pk': board_participant.pk})
    response = get_auth_client.get(path=url)

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_board_detail_with_not_auth_user(board_participant_factory, client):
    board_participant = board_participant_factory()
    url = reverse('board', kwargs={'pk': board_participant.pk})
    response = client.get(path=url)

    assert response.status_code == 403
    assert response.data == {
        'detail': 'Authentication credentials were not provided.'
    }