from uuid import uuid4


def build_unique_courier_payload():
    suffix = uuid4().hex[:10]
    return {
        "login": f"qa_courier_{suffix}",
        "password": f"Pwd_{suffix}",
        "firstName": "Ivan",
    }


def build_courier_login_payload(courier_payload):
    return {
        "login": courier_payload["login"],
        "password": courier_payload["password"],
    }


def with_optional_color(order_payload, color):
    payload = dict(order_payload)
    if color is None:
        payload.pop("color", None)
    else:
        payload["color"] = color
    return payload


DEFAULT_ORDER_PAYLOAD = {
    "firstName": "Ivan",
    "lastName": "Autotest",
    "address": "Test street 1",
    "metroStation": 4,
    "phone": "+7 800 555 35 35",
    "rentTime": 3,
    "deliveryDate": "2026-06-20",
    "comment": "Sprint 7 API test order",
}

COLOR_BLACK = ["BLACK"]
COLOR_GREY = ["GREY"]
COLOR_BLACK_AND_GREY = ["BLACK", "GREY"]
NO_COLOR = None

ORDER_COLOR_CASES = [
    (COLOR_BLACK, "black"),
    (COLOR_GREY, "grey"),
    (COLOR_BLACK_AND_GREY, "black_and_grey"),
    (NO_COLOR, "without_color"),
]

COURIER_CREATION_MISSING_DATA_MESSAGE = (
    "Недостаточно данных для создания учетной записи"
)
COURIER_DUPLICATE_LOGIN_MESSAGE = "Этот логин уже используется"
COURIER_LOGIN_MISSING_DATA_MESSAGE = "Недостаточно данных для входа"
COURIER_ACCOUNT_NOT_FOUND_MESSAGE = "Учетная запись не найдена"
