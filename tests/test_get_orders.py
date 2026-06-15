import allure


@allure.epic("Scooter API")
@allure.feature("Orders list")
class TestGetOrders:
    @allure.title("Get orders returns orders list")
    def test_get_orders_returns_orders_list(self, api_client):
        response = api_client.get_orders()
        response_body = response.json()

        assert response.status_code == 200
        assert "orders" in response_body
        assert isinstance(response_body["orders"], list)
