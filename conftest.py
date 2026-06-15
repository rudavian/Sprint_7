import pytest

from api_client import ScooterApiClient
from data import build_courier_login_payload, build_unique_courier_payload


@pytest.fixture
def api_client():
    return ScooterApiClient()


@pytest.fixture
def courier_payload():
    return build_unique_courier_payload()


@pytest.fixture
def courier_factory(api_client):
    created_couriers = []

    def create_courier(payload=None):
        courier_payload = (
            payload if payload is not None else build_unique_courier_payload()
        )
        response = api_client.create_courier(courier_payload)

        if response.status_code == 201:
            created_couriers.append(dict(courier_payload))

        return response, courier_payload

    yield create_courier

    for payload in created_couriers:
        login_response = api_client.login_courier(
            build_courier_login_payload(payload)
        )

        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            if courier_id is not None:
                api_client.delete_courier(courier_id)


@pytest.fixture
def order_tracks_for_cleanup(api_client):
    tracks = []
    yield tracks

    for track in tracks:
        api_client.cancel_order(track)
