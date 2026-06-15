import pytest

from api_client import ScooterApiClient
from helpers import build_courier_login_payload, build_unique_courier_payload


@pytest.fixture
def api_client():
    return ScooterApiClient()


@pytest.fixture
def courier_payload():
    return build_unique_courier_payload()


@pytest.fixture
def created_courier(api_client):
    payload = build_unique_courier_payload()
    response = api_client.create_courier(payload)
    assert response.status_code == 201

    login_response = api_client.login_courier(build_courier_login_payload(payload))
    assert login_response.status_code == 200
    courier_id = login_response.json()["id"]

    yield payload

    api_client.delete_courier(courier_id)


@pytest.fixture
def courier_ids_for_cleanup(api_client):
    courier_ids = []
    yield courier_ids

    for courier_id in courier_ids:
        api_client.delete_courier(courier_id)


@pytest.fixture
def order_tracks_for_cleanup(api_client):
    tracks = []
    yield tracks

    for track in tracks:
        api_client.cancel_order(track)
