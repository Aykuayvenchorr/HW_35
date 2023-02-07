import pytest
from django.urls import reverse
from rest_framework import status
import datetime

test_date = str(datetime.datetime.now().date())


@pytest.mark.django_db
def test_goal_update(auth_client, goal, test_user, goal_category):
    url = reverse('goal', kwargs={'pk': goal.id})
    expected_response = {
            'title': 'test',
            'category': goal_category.pk,
            'due_date': test_date,
            'description': 'test',
            'status': 1,
            'priority': 1
        }
    response = auth_client.patch(path=url, data=expected_response)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_data['user']['id'] == test_user.pk
    assert response_data['user']['username'] == test_user.username
    assert response_data['user']['email'] == test_user.email

    assert response_data['title'] == expected_response['title']
    assert response_data['category'] == expected_response['category']
    assert response_data['due_date'] == expected_response['due_date']
    assert response_data['description'] == expected_response['description']
    assert response_data['status'] == expected_response['status']
    assert response_data['priority'] == expected_response['priority']