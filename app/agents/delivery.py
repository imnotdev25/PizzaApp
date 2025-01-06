from crewai import Agent, Task
from app.llm import llm
from app.tools.orders import update_order_status
from app.tools.delivery import take_review, assign_delivery_boy


# Delivery Agent
delivery_agent = Agent(
    role="Delivery Coordinator",
    goal="Assign delivery drivers, manage delivery progress, and handle disruptions.",
    backstory=(
        "You are in charge of logistics, ensuring pizzas are delivered promptly. "
        "Handle any delays and keep users informed via the customer support agent."
    ),
    llm = llm
)

# Delivery Agent Task
delivery_task = Task(
    description=(
        "Delivery should take 10 seconds, with notifications for disruptions or delays."
        "Use the order_id, user_id and pizza_id from previous iteration data."
        "Assign a delivery driver using the 'assign_delivery_boy' tool."
        "Take a review of the pizza using the 'take_review' tool."
        "Update the order status to 'Delivered' using the 'update_order_status' tool."
    ),
    expected_output="Greetings! return Return order_id, delivery_boy_id, and review, thanks note",
    tools=[update_order_status, assign_delivery_boy, take_review],
    agent=delivery_agent
)