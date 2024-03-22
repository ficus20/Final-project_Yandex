import sender_stand_request
import data

# Екатерина Семенова, 14-я когорта — Финальный проект. Инженер по тестированию плюс
def test_create_order_success():
    order = sender_stand_request.create_order(data.order_body)
    track = order.json()["track"]
    order_info = sender_stand_request.get_order(track)
    assert order_info.status_code == 200