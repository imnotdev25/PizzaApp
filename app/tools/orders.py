from crewai.tools import tool

from app.db import session
from app.models import Pizza, User, Order, Chef, DeliveryBoy


@tool("get_pizzas")
def get_pizzas():
    """Retrieve the list of available pizzas from the menu."""
    pizzas = session.query(Pizza).all()
    pizza_list = "\n".join([f"{pizza.id} - {pizza.name} - {pizza.description} - ${pizza.price}" for pizza in pizzas])
    return f"Available Pizzas:\n{pizza_list}"


@tool("confirm_order")
def order_confirm():
    """Simulate a callback to confirm the order."""
    confirm = input(f"Confirm your order (yes/no): ").strip().lower()
    return confirm == "yes"


@tool("create_order")
def create_order(user_id: int, pizza_id: int) -> str:
    """Create a new order."""
    user = session.query(User).filter(User.id == user_id).first()
    pizza = session.query(Pizza).filter(Pizza.id == pizza_id).first()

    if not user:
        return "User not found."
    if not pizza:
        return "Pizza not found."
    if user.wallet < pizza.price:
        return "Insufficient wallet balance."

    # Deduct wallet balance
    user.wallet -= pizza.price
    session.commit()

    # Create the order
    new_order = Order(user_id=user_id, pizza_id=pizza_id)
    session.add(new_order)
    session.commit()

    return f"Order created successfully! Order ID: {new_order.id}"


@tool("update_order_status")
def update_order_status(order_id: int, status: str) -> str:
    """Update the status of an order.
    order_id: int
    status: str
    """
    order = session.query(Order).filter(Order.id == order_id).first()
    if not order:
        return "Order not found."

    order.status = status
    session.commit()
    return f"Order {order_id} status updated to '{status}'."

