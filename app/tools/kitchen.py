from app.models import Chef, DeliveryBoy
from crewai.tools import tool
from app.db import session

@tool("assign_chef")
def assign_chef(order_id: int) -> str:
    """Assign a free chef to an order."""
    chef = session.query(Chef).filter(Chef.is_free == True).first()
    if not chef:
        return "No free chef available."

    chef.is_free = False
    chef.current_order_id = order_id
    session.commit()
    return f"Chef {chef.name} assigned to Order {order_id}."


@tool("assign_delivery_boy")
def assign_delivery_boy(order_id: int) -> str:
    """Assign a free delivery boy to an order."""
    delivery_boy = session.query(DeliveryBoy).filter(DeliveryBoy.is_free == True).first()
    if not delivery_boy:
        return "No free delivery boy available."

    delivery_boy.is_free = False
    delivery_boy.current_order_id = order_id
    session.commit()
    return f"Delivery boy {delivery_boy.name} assigned to Order {order_id}."