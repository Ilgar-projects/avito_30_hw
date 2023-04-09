import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_create_selection(client, access_token, user):
    ad_list = AdFactory.create_batch(3)

    data = {
        "name": "Моя подборка",
        "items": [ad.pk for ad in ad_list],
        "owner": user.username
    }
    expected_data = {
        "id": 1,
        "name": "Моя подборка",
        "items": [ad.pk for ad in ad_list],
        "owner": user.username
    }

    response = client.post("/selection/", data, HTTP_AUTHORIZATION="Bearer " + access_token)
    assert response.status_code == 201
    assert response.data == expected_data
