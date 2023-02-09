import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_board_create(user_factory, auth_client):
    user = user_factory()
    data = {
        'title': 'test board',
    }

    get_auth_client = auth_client(user)

    url = reverse('board_create')

    response = get_auth_client.post(
        path=url,
        data=data,
    )

    assert response.status_code == 201

    expected_response = {
        'id': response.data['id'],
        'title': 'test board',
        'is_deleted': False,
        'created': response.data['created'],
        'updated': response.data['updated'],
    }

    assert response.data == expected_response


@pytest.mark.django_db
def test_board_create_with_not_auth_user(client):
    data = {
        'title': 'test board',
    }

    url = reverse('board_create')

    response = client.post(
        path=url,
        data=data,
    )

    assert response.status_code == 403
    assert response.data == {
        'detail': 'Authentication credentials were not provided.'
    }


@pytest.mark.django_db
def test_board_list(user_factory, auth_client, board_participant_factory):
    user = user_factory()
    board_participant = board_participant_factory.create_batch(10, user=user)

    get_auth_client = auth_client(user)
    url = reverse('board_list')
    response = get_auth_client.get(path=url)

    assert response.status_code == 200
    assert len(response.data) == 10
