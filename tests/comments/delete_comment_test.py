import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_goal_comment_delete(user_factory, auth_client, board_participant_factory, goal_comment_factory):
    user = user_factory()
    board_participant = board_participant_factory(user=user)
    goal_comment = goal_comment_factory(
        goal__category__board=board_participant.board,
        goal__category__user=user,
        goal__user=user,
        user=user,
    )

    get_auth_client = auth_client(user)
    url = reverse('comment', kwargs={'pk': goal_comment.pk})
    response = get_auth_client.delete(path=url)

    assert response.status_code == 204
    assert response.data is None