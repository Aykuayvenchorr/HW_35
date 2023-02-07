import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_goal_delete(auth_client, goal):
    url = reverse('goal', kwargs={'pk': goal.id})
    response = auth_client.delete(path=url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
