import pytest
from django.urls import reverse
from rest_framework import status

from goals.serializers import GoalCategorySerializer


@pytest.mark.django_db
def test_create_category(auth_client, test_user, board):
    url = reverse('category_create')
    expected_response = {
            'user': test_user.pk,
            'board': board.pk,
            'title': 'test',
            'is_deleted': True
        }

    response = auth_client.post(
        path=url,
        data=expected_response
    )
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert response_data['board'] == expected_response['board']
    assert response_data['title'] == expected_response['title']
    assert response_data['is_deleted'] == expected_response['is_deleted']
