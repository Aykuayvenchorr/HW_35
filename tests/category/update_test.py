import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_category_update(user_factory, board_participant_factory, auth_client, goal_category_factory):
    user = user_factory()
    board_participant = board_participant_factory(user=user)
    category = goal_category_factory(board=board_participant.board, user=user)
    url = reverse('category', kwargs={'pk': category.id})
    get_client = auth_client(user=user)
    data = {
        "title": "test goal!",
    }

    response = get_client.put(path=url, data=data)
    # response_data = response.json()

    expected_response = {
        "id": category.id,
        "title": "test goal!",
        "is_deleted": False,
        "board": category.board.id,
        "created": category.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        "updated": response.data["updated"],
        "user": {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        },
    }
    # expected_response = {
    #     'title': 'test goal!',
    #     'is_deleted': False,
    #     'user': {
    #         'id': user.id,
    #         'username': user.username,
    #         'first_name': user.first_name,
    #         'last_name': user.last_name,
    #         'email': user.email}}
    # # 'board':

    # response = get_client.patch(path=url, data=data)
    # response_data = response.json()

    assert response.status_code == 200
    # assert response_data['user']['id'] == test_user.pk
    # assert response_data['user']['username'] == test_user.username
    # assert response_data['user']['email'] == test_user.email
    assert response.data == expected_response
    # assert response_data['is_deleted'] == expected_response['is_deleted']
    # assert response_data['board'] == category.board_id
