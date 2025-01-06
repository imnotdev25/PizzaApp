from crewai import Agent, Task
from app.llm import llm


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
        "Assign a delivery driver, track delivery progress, and update the user via Agent 1. "
        "Delivery should take 10 seconds, with notifications for disruptions or delays."
    ),
    expected_output="Order is marked as delivered and user is notified.",
    agent=delivery_agent
)