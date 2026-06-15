import allure
import requests

from urls import (
    BASE_URL,
    CANCEL_ORDER_PATH,
    CREATE_COURIER_PATH,
    CREATE_ORDER_PATH,
    DELETE_COURIER_PATH_TEMPLATE,
    GET_ORDERS_PATH,
    LOGIN_COURIER_PATH,
)

DEFAULT_TIMEOUT = 20


class ScooterApiClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def _url(self, path):
        return f"{self.base_url}{path}"

    @allure.step("Создать курьера")
    def create_courier(self, payload):
        return self.session.post(
            self._url(CREATE_COURIER_PATH),
            json=payload,
            timeout=DEFAULT_TIMEOUT,
        )

    @allure.step("Авторизовать курьера")
    def login_courier(self, payload):
        return self.session.post(
            self._url(LOGIN_COURIER_PATH),
            json=payload,
            timeout=DEFAULT_TIMEOUT,
        )

    @allure.step("Удалить курьера")
    def delete_courier(self, courier_id):
        path = DELETE_COURIER_PATH_TEMPLATE.format(courier_id=courier_id)
        return self.session.delete(self._url(path), timeout=DEFAULT_TIMEOUT)

    @allure.step("Создать заказ")
    def create_order(self, payload):
        return self.session.post(
            self._url(CREATE_ORDER_PATH),
            json=payload,
            timeout=DEFAULT_TIMEOUT,
        )

    @allure.step("Получить список заказов")
    def get_orders(self, params=None):
        return self.session.get(
            self._url(GET_ORDERS_PATH),
            params=params,
            timeout=DEFAULT_TIMEOUT,
        )

    @allure.step("Отменить заказ")
    def cancel_order(self, track):
        # This endpoint accepts the order track as a query parameter.
        return self.session.put(
            self._url(CANCEL_ORDER_PATH),
            params={"track": track},
            timeout=DEFAULT_TIMEOUT,
        )
