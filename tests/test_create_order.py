import allure
import pytest

from data import DEFAULT_ORDER_PAYLOAD, ORDER_COLOR_CASES
from helpers import with_optional_color


@allure.epic("Scooter API")
@allure.feature("Order creation")
class TestCreateOrder:
    @allure.title("Create order with color variant returns track")
    @pytest.mark.parametrize(
        "color, case_name",
        ORDER_COLOR_CASES,
        ids=[case_name for _, case_name in ORDER_COLOR_CASES],
    )
    def test_create_order_with_color_variant_returns_track(
        self,
        api_client,
        order_tracks_for_cleanup,
        color,
        case_name,
    ):
        order_payload = with_optional_color(DEFAULT_ORDER_PAYLOAD, color)
        response = api_client.create_order(order_payload)
        response_body = response.json()

        assert response.status_code == 201
        assert "track" in response_body
        assert isinstance(response_body["track"], int)

        order_tracks_for_cleanup.append(response_body["track"])
