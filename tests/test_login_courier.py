import allure
import pytest

from data import (
    COURIER_ACCOUNT_NOT_FOUND_MESSAGE,
    COURIER_LOGIN_MISSING_DATA_MESSAGE,
    build_courier_login_payload,
    build_unique_courier_payload,
)


@allure.epic("Scooter API")
@allure.feature("Courier login")
class TestLoginCourier:
    @allure.title("Login courier with valid credentials returns id")
    def test_login_courier_with_valid_credentials_returns_id(
        self,
        api_client,
        courier_factory,
    ):
        create_response, courier_payload = courier_factory()
        assert create_response.status_code == 201

        response = api_client.login_courier(
            build_courier_login_payload(courier_payload)
        )
        response_body = response.json()

        assert response.status_code == 200
        assert "id" in response_body
        assert isinstance(response_body["id"], int)

    @allure.title("Login courier without login returns error")
    @pytest.mark.parametrize("missing_field", ["login"])
    def test_login_courier_without_required_login_returns_error(
        self,
        api_client,
        courier_factory,
        missing_field,
    ):
        create_response, courier_payload = courier_factory()
        assert create_response.status_code == 201

        login_payload = build_courier_login_payload(courier_payload)
        login_payload.pop(missing_field)
        response = api_client.login_courier(login_payload)
        response_body = response.json()

        assert response.status_code == 400
        assert response_body["message"] == COURIER_LOGIN_MISSING_DATA_MESSAGE

    @allure.title("Login courier with incorrect password returns error")
    def test_login_courier_with_incorrect_password_returns_error(
        self,
        api_client,
        courier_factory,
    ):
        create_response, courier_payload = courier_factory()
        assert create_response.status_code == 201

        login_payload = build_courier_login_payload(courier_payload)
        login_payload["password"] = "incorrect_password"
        response = api_client.login_courier(login_payload)
        response_body = response.json()

        assert response.status_code == 404
        assert response_body["message"] == COURIER_ACCOUNT_NOT_FOUND_MESSAGE

    @allure.title("Login nonexistent courier returns error")
    def test_login_nonexistent_courier_returns_error(self, api_client):
        response = api_client.login_courier(
            build_courier_login_payload(build_unique_courier_payload())
        )
        response_body = response.json()

        assert response.status_code == 404
        assert response_body["message"] == COURIER_ACCOUNT_NOT_FOUND_MESSAGE
