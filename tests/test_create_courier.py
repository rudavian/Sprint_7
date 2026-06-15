import allure
import pytest

from data import (
    COURIER_CREATION_MISSING_DATA_MESSAGE,
    COURIER_DUPLICATE_LOGIN_MESSAGE,
)


@allure.epic("Scooter API")
@allure.feature("Courier creation")
class TestCreateCourier:
    @allure.title("Create courier with required fields returns ok true")
    def test_create_courier_with_required_fields_returns_ok_true(
        self,
        courier_factory,
    ):
        response, _ = courier_factory()
        response_body = response.json()

        assert response.status_code == 201
        assert response_body == {"ok": True}

    @allure.title("Create courier with existing login returns error")
    def test_create_courier_with_existing_login_returns_error(
        self,
        courier_factory,
    ):
        create_response, courier_payload = courier_factory()
        assert create_response.status_code == 201

        response, _ = courier_factory(courier_payload)
        response_body = response.json()

        assert response.status_code == 409
        assert COURIER_DUPLICATE_LOGIN_MESSAGE in response_body["message"]

    @allure.title("Create courier without login or password returns error")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_login_or_password_returns_error(
        self,
        courier_factory,
        courier_payload,
        missing_field,
    ):
        courier_payload.pop(missing_field)
        response, _ = courier_factory(courier_payload)
        response_body = response.json()

        assert response.status_code == 400
        assert response_body["message"] == COURIER_CREATION_MISSING_DATA_MESSAGE
