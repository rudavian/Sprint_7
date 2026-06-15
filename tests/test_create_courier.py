import allure
import pytest

from data import (
    COURIER_CREATION_MISSING_DATA_MESSAGE,
    COURIER_DUPLICATE_LOGIN_MESSAGE,
)
from helpers import build_courier_login_payload


@allure.epic("Scooter API")
@allure.feature("Courier creation")
class TestCreateCourier:
    @allure.title("Create courier with required fields returns ok true")
    def test_create_courier_with_required_fields_returns_ok_true(
        self,
        api_client,
        courier_payload,
        courier_ids_for_cleanup,
    ):
        response = api_client.create_courier(courier_payload)
        response_body = response.json()

        assert response.status_code == 201
        assert response_body == {"ok": True}

        login_response = api_client.login_courier(
            build_courier_login_payload(courier_payload)
        )
        courier_ids_for_cleanup.append(login_response.json()["id"])

    @allure.title("Create courier with existing login returns error")
    def test_create_courier_with_existing_login_returns_error(
        self,
        api_client,
        created_courier,
    ):
        response = api_client.create_courier(created_courier)
        response_body = response.json()

        assert response.status_code == 409
        assert COURIER_DUPLICATE_LOGIN_MESSAGE in response_body["message"]

    @allure.title("Create courier without login or password returns error")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_login_or_password_returns_error(
        self,
        api_client,
        courier_payload,
        missing_field,
    ):
        courier_payload.pop(missing_field)
        response = api_client.create_courier(courier_payload)
        response_body = response.json()

        assert response.status_code == 400
        assert response_body["message"] == COURIER_CREATION_MISSING_DATA_MESSAGE
