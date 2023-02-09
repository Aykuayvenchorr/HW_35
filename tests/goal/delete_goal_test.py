import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_goal_delete(user_factory, auth_client, goal_factory, board_participant_factory):
    user = user_factory()
    board_participant = board_participant_factory(user=user)
    goal = goal_factory(
        category__board=board_participant.board, category__user=user, user=user)

    get_auth_client = auth_client(user)
    url = reverse('goal', kwargs={'pk': goal.id})
    response = get_auth_client.delete(path=url)

    assert response.status_code == 204
    assert response.data is None
