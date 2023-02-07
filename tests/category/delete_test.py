import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_category_delete(auth_client, goal_category):
    url = reverse('category', kwargs={'pk': goal_category.id})

    response = auth_client.delete(path=url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
