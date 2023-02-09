import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_category_delete(user_factory, board_participant_factory, auth_client, goal_category_factory):
    user = user_factory()
    board_participant = board_participant_factory(user=user)
    category = goal_category_factory(board=board_participant.board, user=user)
    url = reverse('category', kwargs={'pk': category.id})
    get_client = auth_client(user=user)
    response = get_client.delete(path=url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
