import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_category_update(auth_client, test_user, goal_category):
    url = reverse('category', kwargs={'pk': goal_category.id})
    expected_response = {
            'title': 'test',
            'is_deleted': True
        }

    response = auth_client.patch(path=url, data=expected_response)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_data['user']['id'] == test_user.pk
    assert response_data['user']['username'] == test_user.username
    assert response_data['user']['email'] == test_user.email
    assert response_data['title'] == expected_response['title']
    assert response_data['is_deleted'] == expected_response['is_deleted']
    assert response_data['board'] == goal_category.board_id