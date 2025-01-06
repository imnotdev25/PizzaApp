from app.agents.order import user_agent, user_task
from app.agents.delivery import delivery_agent, delivery_task
from app.agents.kitchen import kitchen_agent, kitchen_task
from crewai import Crew, Process

# --- Crew Definitions ---
order_crew = Crew(
    agents=[user_agent, kitchen_agent, delivery_agent],
    tasks=[user_task, kitchen_task, delivery_task],
    process=Process.sequential,
    verbose=True
)
