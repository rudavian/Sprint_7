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
