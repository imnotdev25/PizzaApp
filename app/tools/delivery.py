from app.models import Chef, DeliveryBoy, Order
from crewai.tools import tool
from app.db import session


@tool("assign_delivery_boy")
def assign_delivery_boy(order_id: int) -> str:
    """Assign a free delivery boy to an order."""
    delivery_boy = session.query(DeliveryBoy).filter(DeliveryBoy.is_free == True).first()
    if not delivery_boy:
        return "No free delivery boy available."
    order = session.query(Order).filter(Order.id == order_id).first()
    order.delivery_boy_id = delivery_boy.id
    delivery_boy.is_free = False
    session.commit()
    return f"Delivery boy {delivery_boy.name} assigned to Order {order_id}."


@tool("take_review")
def take_review(order_id: int) -> str:
    """Take review for an order."""
    review = input("Enter order review: ")
    order = session.query(Order).filter(Order.id == order_id).first()
    order.review = review
    session.commit()
    return f"Review taken for Order {order_id}. \n Review: {review}"