import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_board_delete(auth_client, board_participant):
    get_auth_client = auth_client(board_participant.user)
    url = reverse('board', kwargs={'pk': board_participant.pk})
    response = get_auth_client.delete(path=url)

    assert response.status_code == 204
    assert response.data is None