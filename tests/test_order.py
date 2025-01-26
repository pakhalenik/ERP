from entities.order import Order

def test_order():
    order = Order(order_id=1, quantity=2, rush=True)
    order.set_status("In Progress")
    order.set_estimated_completion_time(30)
    assert order.calculate_priority() == 1
    assert order.status == "In Progress"
    print(order)

test_order()
