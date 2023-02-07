import datetime

import pytest
from django.urls import reverse
from rest_framework import status

from goals.serializers import GoalSerializer

test_date = str(datetime.datetime.now().date())


@pytest.mark.django_db
def test_goal_create(auth_client, goal_category):
    url = reverse('goal_create')

    expected_response = {
            'title': 'test',
            'category': goal_category.pk,
            'due_date': test_date,
            'description': 'test',
            'status': 1,
            'priority': 1
        }
    response = auth_client.post(
        path=url,
        data=expected_response
    )
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert response_data['title'] == expected_response['title']
    assert response_data['category'] == expected_response['category']
    assert response_data['due_date'] == expected_response['due_date']
    assert response_data['description'] == expected_response['description']
    assert response_data['status'] == expected_response['status']
    assert response_data['priority'] == expected_response['priority']


@pytest.mark.django_db
def test_goal_list(auth_client, goal_list):
    url = reverse('goal_list')

    response = auth_client.get(path=url)
    expected_response = GoalSerializer(goal_list, many=True).data

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response

