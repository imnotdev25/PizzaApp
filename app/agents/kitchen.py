from crewai import Agent, Task
from app.llm import llm
from app.tools.orders import update_order_status
from app.tools.kitchen import assign_chef


# Kitchen Agent
kitchen_agent = Agent(
    role="Kitchen Manager",
    goal="Manage the pizza cooking process and update order status.",
    backstory=(
        "You are responsible for coordinating the kitchen operations. "
        "Ensure pizzas are cooked and ready for delivery on time."
    ),
    llm = llm
)


# Kitchen Agent Task
kitchen_task = Task(
    description=(
        "Accept the order and process it through stages: accepted → cooking → ready for delivery. "
        "Each stage should be updated in 10-second intervals."
        "Use the order_id, user_id, and pizza_id from iteration data."
        "Update the order status to 'accepted' after 10 seconds, use update_order_status tool."
        "Assign a chef to the order use assign_chef tool and update the status using update_order_status to 'cooking' after 10 seconds."
        "Update the status to 'ready for delivery' after 10 seconds, use update_order_status tool."
    ),
    expected_output="Order is marked as ready for delivery after cooking.",
    tools=[update_order_status, assign_chef],
    agent=kitchen_agent
)
